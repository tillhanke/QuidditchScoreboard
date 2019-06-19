using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QuidditchScoreboard
{
    class Class1
    {
        public class Rootobject
        {
            public string status { get; set; }
            public Data data { get; set; }
        }

        public class Data
        {
            public string public_id { get; set; }
            public string description { get; set; }
            public object pitch { get; set; }
            public object specification { get; set; }
            public object group { get; set; }
            public int time { get; set; }
            public bool data_available { get; set; }
            public bool switched { get; set; }
            public string active_period { get; set; }
            public int alive_timestamp { get; set; }
            public int tournament { get; set; }
            public int delay { get; set; }
            public bool cancelled { get; set; }
            public object cancelled_reason { get; set; }
            public bool suspended { get; set; }
            public object suspended_reason { get; set; }
            public Teams teams { get; set; }
            public Gametime gametime { get; set; }
            public bool game_over { get; set; }
            public Score score { get; set; }
            public Events events { get; set; }
        }

        public class Teams
        {
            public A A { get; set; }
            public B B { get; set; }
        }

        public class A
        {
            public string name { get; set; }
            public string shortname { get; set; }
            public string jersey { get; set; }
            public string jerseyPrimaryColor { get; set; }
            public string jerseySecondaryColor { get; set; }
            public string jerseyTextColor { get; set; }
            public string logo { get; set; }
        }

        public class B
        {
            public string name { get; set; }
            public string shortname { get; set; }
            public string jersey { get; set; }
            public string jerseyPrimaryColor { get; set; }
            public string jerseySecondaryColor { get; set; }
            public string jerseyTextColor { get; set; }
            public string logo { get; set; }
        }

        public class Gametime
        {
            public Regular regular { get; set; }
            public Firstot firstOT { get; set; }
            public Secondot secondOT { get; set; }
        }

        public class Regular
        {
            public int gametimeLastStop_ms { get; set; }
            public object timeAtLastStart_ms { get; set; }
            public bool running { get; set; }
        }

        public class Firstot
        {
            public int periodLength_ms { get; set; }
            public object gameDurationLastStop_ms { get; set; }
            public object timeAtLastStart_ms { get; set; }
            public object running { get; set; }
        }

        public class Secondot
        {
            public object gametimeLastStop_ms { get; set; }
            public object timeAtLastStart_ms { get; set; }
            public object running { get; set; }
        }

        public class Score
        {
            public A1 A { get; set; }
            public B1 B { get; set; }
        }

        public class A1
        {
            public Regular1 regular { get; set; }
            public Firstot1 firstOT { get; set; }
            public Secondot1 secondOT { get; set; }
        }

        public class Regular1
        {
            public int quaffelPoints { get; set; }
            public bool snitchCaught { get; set; }
            public int snitchPoints { get; set; }
        }

        public class Firstot1
        {
            public object quaffelPoints { get; set; }
            public object snitchCaught { get; set; }
            public object snitchPoints { get; set; }
        }

        public class Secondot1
        {
            public object quaffelPoints { get; set; }
            public object snitchCaught { get; set; }
            public object snitchPoints { get; set; }
        }

        public class B1
        {
            public Regular2 regular { get; set; }
            public Firstot2 firstOT { get; set; }
            public Secondot2 secondOT { get; set; }
        }

        public class Regular2
        {
            public int quaffelPoints { get; set; }
            public bool snitchCaught { get; set; }
            public int snitchPoints { get; set; }
        }

        public class Firstot2
        {
            public object quaffelPoints { get; set; }
            public object snitchCaught { get; set; }
            public object snitchPoints { get; set; }
        }

        public class Secondot2
        {
            public object quaffelPoints { get; set; }
            public object snitchCaught { get; set; }
            public object snitchPoints { get; set; }
        }

        public class Events
        {
            public Score1[] score { get; set; }
            public Timeout[] timeout { get; set; }
            public Snitch[] snitch { get; set; }
            public Penalty[] penalty { get; set; }
        }

        public class Score1
        {
            public string period { get; set; }
            public string team { get; set; }
            public int gametime { get; set; }
            public int stacked_gametime { get; set; }
            public string player_number { get; set; }
            public object player_name { get; set; }
        }

        public class Timeout
        {
            public string period { get; set; }
            public string team { get; set; }
            public int gametime { get; set; }
            public int stacked_gametime { get; set; }
        }

        public class Snitch
        {
            public string period { get; set; }
            public string team { get; set; }
            public int gametime { get; set; }
            public int stacked_gametime { get; set; }
            public object player_number { get; set; }
            public object player_name { get; set; }
        }

        public class Penalty
        {
            public string color { get; set; }
            public int increment { get; set; }
            public string period { get; set; }
            public string team { get; set; }
            public int gametime { get; set; }
            public int stacked_gametime { get; set; }
            public string player_number { get; set; }
            public string player_name { get; set; }
            public string reason { get; set; }
        }

    }
}
