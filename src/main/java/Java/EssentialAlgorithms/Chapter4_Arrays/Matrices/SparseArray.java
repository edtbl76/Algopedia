package Java.EssentialAlgorithms.Chapter4_Arrays.Matrices;

public class SparseArray<T extends Number> {

    private class ArrayRow {
        private int rowId;
        private ArrayRow next;
        private Entry sentinel;

        public ArrayRow() {}

        public int getRowId() {
            return rowId;
        }

        public void setRowId(int rowId) {
            this.rowId = rowId;
        }

        public ArrayRow getNext() {
            return next;
        }

        public void setNext(ArrayRow next) {
            this.next = next;
        }

        public Entry getSentinel() {
            return sentinel;
        }

        public void setSentinel(Entry sentinel) {
            this.sentinel = sentinel;
        }
    }

    private class Entry {
        private int colId;
        private Entry next;
        private T value;

        public int getColId() {
            return colId;
        }

        public void setColId(int colId) {
            this.colId = colId;
        }

        public Entry getNext() {
            return next;
        }

        public void setNext(Entry next) {
            this.next = next;
        }

        public T getValue() {
            return value;
        }

        public void setValue(T value) {
            this.value = value;
        }
    }

    private T default_value;
    private ArrayRow head;

    public SparseArray(T default_value) {
        this.default_value = default_value;
        head = new ArrayRow();
        head.setNext(null);
    }

    private T get(int row, int col) {
        Entry entry = getEntry(row, col, false);
        if (entry == null)
            return default_value;

        return entry.getValue();
    }

    void set(int row, int col, T value) {
        if (value.equals(default_value))
            removeEntry(row, col);
        else {
            Entry entry = getEntry(row, col, true);
            entry.setValue(value);
        }
    }

    // ===== Helper Code
    private ArrayRow getRowBefore(int row) {
        ArrayRow arrayRow = head;
        while ((arrayRow.getNext() != null) && (arrayRow.getNext().getRowId() < row))
            arrayRow = arrayRow.getNext();
        return arrayRow;
    }

    private ArrayRow getRow(int row, boolean create) {
        ArrayRow before = getRowBefore(row);
        if ((before.getNext() != null) && (before.getNext().getRowId() == row))
            return before.getNext();

        if (create) {
            ArrayRow newRow = new ArrayRow();
            newRow.setRowId(row);

            newRow.setNext(before.getNext());
            before.setNext(newRow);

            newRow.setSentinel(new Entry());
            newRow.getSentinel().setNext(null);

            return newRow;
        }

        return null;
    }

    private Entry getColumnBefore(Entry entry, int col) {
        while ((entry.getNext() != null) && (entry.getNext().getColId() < col))
            entry = entry.getNext();

        return entry;
    }

    private Entry getColumn(Entry entry, int col, boolean create) {
        Entry before = getColumnBefore(entry ,col);
        if ((before.getNext() != null) && (before.getNext().getColId() == col))
            return before.getNext();

        if (create) {
            Entry newEntry = new Entry();
            newEntry.setColId(col);

            newEntry.setNext(before.getNext());
            before.setNext(newEntry);

            return newEntry;
        }
        return null;
    }

    /**
     * DONT DO THIS. I'm putting this in here just to make the demo work. We'd probably have to create subclasses
     * of this class that are numeral specific in order to perform math operations.
     */
    private <T extends Number> T addVals(T x, T y) {
        Integer sum = x.intValue() + y.intValue();
        return (T) sum;
    }


    private Entry getEntry(int row, int col, boolean create) {
        ArrayRow arrayRow = getRow(row, create);
        if (arrayRow == null)
            return null;

        return getColumn(arrayRow.getSentinel(), col, create);
    }

    private void removeEntry(int row, int col) {
        // get row and before Row If we don't find row .. bail out.
        ArrayRow beforeRow = getRowBefore(row);
        ArrayRow arrayRow = beforeRow.getNext();
        if ((arrayRow.getNext() == null) || arrayRow.getRowId() != row)
            return;

        // get before col & col. If we dont' find entry... bail out
        Entry beforeEntry = getColumnBefore(arrayRow.getSentinel(), col);
        Entry entry = beforeEntry.getNext();
        if((entry.getNext() == null) || (entry.getColId() != col))
            return;

        // bust the links
        beforeEntry.setNext(entry.getNext());

        Entry arrayHead = arrayRow.getSentinel();
        if (arrayHead.getNext() == null) {
            beforeRow.setNext(arrayRow.getNext());
        }
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        ArrayRow row = head.getNext();
        while (row != null) {
            Entry value = row.getSentinel().getNext();
            while (value != null) {
                builder
                        .append(" (").append(row.getRowId())
                        .append(",").append(value.getColId())
                        .append(")").append(value.getValue())
                        .append(" ");
                value = value.getNext();
            }
            row = row.getNext();
        }
        return String.valueOf(builder);
    }

    private void copyEntries(Entry fromEntry, Entry toEntry) {
        while (fromEntry != null) {
            toEntry.setNext(new Entry());
            toEntry = toEntry.getNext();
            toEntry.setColId(fromEntry.getColId());
            toEntry.setValue(fromEntry.getValue());
            toEntry.setNext(null);

            fromEntry = fromEntry.getNext();
        }
    }

    private void addEntries(Entry from1, Entry from2, Entry sum) {
        while ((from1 != null) && (from2 != null)) {

            sum.setNext(new Entry());
            sum = sum.getNext();

            // copy smaller of 2 entries or both if equal
            if (from1.getColId() < from2.getColId()) {
                sum.setColId(from1.getColId());
                sum.setValue(from1.getValue());
                from1 = from1.getNext();
            } else if (from1.getColId() > from2.getColId()) {
                sum.setColId(from2.getColId());
                sum.setValue(from2.getValue());
                from2 = from2.getNext();
            } else {
                sum.setColId(from1.getColId());
                sum.setValue(addVals(from1.getValue(), from2.getValue()));
                from1 = from1.getNext();
                from2 = from2.getNext();
            }

        }

        // Add rest of entries from list that aren't empty
        if (from1 != null)
            copyEntries(from1, sum);
        if (from2 != null)
            copyEntries(from2, sum);
    }

    /**
        This is the bread and butter of the matrix math piece.
        - here we are going to add two sparse arrays together.
     */
    public SparseArray<T> add(SparseArray<T> array) {

        SparseArray<T> result = new SparseArray<>(default_value);

        // set up vars
        ArrayRow thisRow = this.head.getNext();
        ArrayRow thatRow = array.head.getNext();
        ArrayRow resultRow = result.head;

        while ((thisRow != null && (thatRow != null))) {

            // Build result
            resultRow.setNext(new ArrayRow());
            resultRow = resultRow.getNext();
            resultRow.setSentinel(new Entry());

            // Copy lesser of the two or both if equal
            if (thisRow.getRowId() < thatRow.getRowId()) {
                resultRow.setRowId(thisRow.getRowId());
                copyEntries(thisRow.getSentinel().getNext(), resultRow.getSentinel());
                thisRow = thisRow.getNext();
            } else if (thisRow.getRowId() > thatRow.getRowId()) {
                resultRow.setRowId(thatRow.getRowId());
                copyEntries(thatRow.getSentinel().getNext(), resultRow.getSentinel());
                thatRow = thatRow.getNext();
            } else {
                resultRow.setRowId(thisRow.getRowId());
                addEntries(thisRow.getSentinel().getNext(), thatRow.getSentinel().getNext(), resultRow.getSentinel());
                thisRow = thisRow.getNext();
                thatRow = thatRow.getNext();
            }
        }

        // add the remaining rows
        while (thisRow != null) {
            resultRow.setNext(new ArrayRow());
            resultRow = resultRow.getNext();
            resultRow.setRowId(thisRow.getRowId());
            resultRow.setSentinel(new Entry());
            resultRow.setNext(null);

            copyEntries(thisRow.getSentinel().getNext(), resultRow.getSentinel());
            thisRow = thisRow.getNext();
        }
        while (thatRow != null) {
            resultRow.setNext(new ArrayRow());
            resultRow = resultRow.getNext();
            resultRow.setRowId(thatRow.getRowId());
            resultRow.setSentinel(new Entry());
            resultRow.setNext(null);

            copyEntries(thatRow.getSentinel().getNext(), resultRow.getSentinel());
            thatRow = thatRow.getNext();
        }

        return result;
    }
}

class ArrayValue<T> {
    private int row;
    private int col;
    private T value;

    public int getRow() {
        return row;
    }

    public void setRow(int row) {
        this.row = row;
    }

    public int getCol() {
        return col;
    }

    public void setCol(int col) {
        this.col = col;
    }

    public T getValue() {
        return value;
    }

    public void setValue(T value) {
        this.value = value;
    }
}