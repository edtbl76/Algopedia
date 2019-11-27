package Java.EssentialAlgorithms.Chapter4_Arrays.SparseArrays;

public class SparseArray<T> {

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

    public T get(int row, int col) {
        Entry entry = getEntry(row, col, false);
        if (entry == null)
            return default_value;

        return entry.getValue();
    }

    public void set(int row, int col, T value) {
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