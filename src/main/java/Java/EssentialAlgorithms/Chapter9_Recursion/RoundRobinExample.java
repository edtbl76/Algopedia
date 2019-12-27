package Java.EssentialAlgorithms.Chapter9_Recursion;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.ArrayList;
import java.util.List;

public class RoundRobinExample {

    public static void main(String[] args) {
        int number_of_teams = ExecUtils.getRandom(6,2);
        List<String> teams = setTeams(number_of_teams);

        List<List<MatchUp>> schedule = roundRobin(teams);
        schedule.forEach(matchUps -> {
            System.out.println("Week: " + (schedule.indexOf(matchUps) + 1));
            StringBuilder sb = new StringBuilder();
            matchUps.forEach(matchUp -> {

                sb.append("\t").append(matchUp).append("\t\t");

                if ((matchUps.indexOf(matchUp) + 1) % 5 == 0)
                    sb.append('\n');
            });
            System.out.println(sb);
        });

    }

    static List<String> setTeams(int num) {
        List<String> names = new ArrayList<>();
        for(int i = 0; i < num; i++)
            names.add(i, String.format("Team%2d", i + 1));
        return names;
    }

    static List<List<MatchUp>> roundRobin(List<String> teams) {
        String bye = "BYEW";
        // If number of teams is even, swap out BYEW with the first team, and then yank that team out of the List.,
        if (teams.size() % 2 == 0) {
            bye = teams.get(0);
            teams.remove(0);
        }

        return oddSchedule(teams, bye);
    }

    static List<List<MatchUp>> oddSchedule(List<String> teams, String bye) {
        int num = teams.size();
        int mid = num / 2;

        List<List<MatchUp>> schedule = new ArrayList<>();

        /*
            Outer loop is the round generator.
         */
        for (int i = 0; i < num; i++) {
            System.out.println("bye: " + bye);
            List<MatchUp> round = new ArrayList<>();
            System.out.println("Adding Round" + (i + 1));

            /*
                Inner Loop generates the match ups by working out from either end of the list to the middle.
             */
            for (int j = 1; j <= mid; j++) {
                System.out.println("\tAdding: " + teams.get(j) + " " + teams.get(num - j));
                round.add(new MatchUp(teams.get(j), teams.get(num - j)));
            }
            /*
                Here we handle the bye week. Whatever team was at 0 we skip, and gets a bye week or matched w/
                the bye team.
             */
            System.out.println("\t\tByeWeek: " + teams.get(0));
            round.add(new MatchUp(teams.get(0), bye));
            schedule.add(round);

            /*
                This takes the last item of the list and moves it to the front.
                Since the outer loop iterates over the entire size of the list, but the inner loop iterates
                towards the middle, we'll end up with 1 matchup for each team.
             */
            System.out.println("\t\tMoving " + teams.get(num - 1));
            teams.add(0, teams.get(num - 1));
            System.out.println("\t\tRemoving " + teams.get(num));
            teams.remove(num);
        }
        return schedule;
    }

}

class MatchUp {
    public String team1;
    public String team2;

    public MatchUp(String team1, String team2) {
        this.team1 = team1;
        this.team2 = team2;
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder();
        sb.append(team1).append(" vs ").append(team2);
        return sb.toString();
    }
}
