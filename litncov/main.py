import argparse
from rich.console import Console
from litncov.user import litUesr
from litncov import util


def main():
    console = Console()

    parser = argparse.ArgumentParser(
        description="A ncov cli tool for LIT(Luoyang Institute of Science and Technology)",
        epilog="(c) 2020 icepie.dev@gmail.com",
    )
    parser.add_argument("-u", "--username", help="the username", required=True)
    parser.add_argument("-p", "--password", help="the password", required=True)

    subparsers = parser.add_subparsers(dest="command")

    # report command
    report = subparsers.add_parser("report", help="run the report action")
    report.add_argument(
        "-a", "--all", action="store_true", help="do the all report tasks today"
    )
    report.add_argument("-f", "--force", action="store_true", help="forcely report")
    report.add_argument("-r", "--rtime", help="the report time {1,2,3}, default 'last'")
    report.add_argument(
        "-m",
        "--mode",
        help="the report mode {'last', 'random', 'manual'}, default 'last'",
    )
    report.add_argument("-t", "--temp", help="the body temperature (float)")

    # info command
    info = subparsers.add_parser("info", help="get the user info")
    info.add_argument("-u", "--user", action="store_true", help="the user main info")
    info.add_argument(
        "-l", "--last_record", action="store_true", help="the user last record info"
    )
    info.add_argument(
        "-f", "--family", action="store_true", help="the user family info"
    )
    info.add_argument(
        "-i", "--instructor", action="store_true", help="the user instructor info"
    )
    info.add_argument("-t", "--tirp", action="store_true", help="the user tirp info")

    query = subparsers.add_parser("query", help="query history of the user report")
    query.add_argument(
        "-s",
        "--start_time",
        help="the start time of the report history (Year-Month-Day)",
        required=True,
    )
    query.add_argument(
        "-e",
        "--end_time",
        help="the end time of the report history, default Today (Year-Month-Day)",
    )

    args = parser.parse_args()

    # check the command
    if not args.command or args.command not in {"report", "info", "query"}:
        parser.print_help()
        exit()

    # new a lit user obj
    testme = litUesr(args.username, args.password)

    # the report main
    if testme.is_logged:
        console.log("[bold cyan]Login successful[/bold cyan]")

        if args.command == "report":

            # check mode arg
            if args.mode and args.mode not in {"last", "random", "manual"}:
                parser.print_help()
                exit()

            # check arg all with rtime
            if args.all and args.rtime:
                console.log(
                    "[bold red]Error: [u]-a[/u] parameter can run with [u]-r[/u] parameter[/bold red]"
                )
                parser.print_help()
                exit()

            # check rtime arg
            if args.rtime and int(args.rtime) not in {1, 2, 3}:
                parser.print_help()
                exit()
            elif not args.rtime and not args.all:
                args.rtime = 1

            # check arg temp with mode
            if args.temp and not args.mode:
                args.mode = "manual"

            if not args.mode:
                args.mode = "last"

            if (args.mode != "manual") and args.temp:
                console.log(
                    "[bold red]Error: only manual mode can run with [u]-t[/u] parameter[/bold red]"
                )
                parser.print_help()
                exit()

            if args.temp and (float(args.temp) >= 37.3 or float(args.temp) < 35.0):
                console.log("[bold red]Dangerous body temperature[/bold red]")
                console.log(
                    "[bold red]If this is your body temperature is too high or low, plz use the [u]-f[/u] parameter to report[/bold red]"
                )
                exit()

            # start report
            # all arg
            if args.all:
                if not testme.is_record_today(3) or args.force:
                    if args.mode == "manual":
                        console.log(
                            testme.first_record(
                                mode=args.mode,
                                rtimes=3,
                                temperature=args.temp,
                                temperatureTwo=args.temp,
                                temperatureThree=args.temp,
                            )
                        )
                    else:
                        console.log(testme.first_record(mode=args.mode, rtimes=3))
                elif args.all:
                    console.log("You have finished all report tasks today")

            # rtime arg
            if args.rtime:
                if int(args.rtime) == 1 and (
                    not testme.is_record_today(1) or args.force
                ):
                    if args.mode == "manual":
                        console.log(
                            testme.first_record(mode=args.mode, temperature=args.temp)
                        )
                    else:
                        console.log(testme.first_record(mode=args.mode))
                elif int(args.rtime) == 2 and (
                    not testme.is_record_today(2) or args.force
                ):
                    if args.mode == "manual":
                        console.log(
                            testme.second_record(mode=args.mode, temperature=args.temp)
                        )
                    else:
                        console.log(testme.second_record(mode=args.mode))
                elif int(args.rtime) == 3 and (
                    not testme.is_record_today(3) or args.force
                ):
                    if args.mode == "manual":
                        console.log(
                            testme.third_record(mode=args.mode, temperature=args.temp)
                        )
                    else:
                        console.log(testme.third_record(mode=args.mode))
                elif args.rtime:
                    console.log(
                        "You have finished the report task %s today" % args.rtime
                    )
        elif args.command == "info":
            if args.user:
                console.log(testme.info)
            if args.last_record:
                console.log(testme.get_last_record())
            if args.family:
                console.log(testme.get_familys())
            if args.instructor:
                console.log(testme.get_instructor())
            if args.tirp:
                console.log(testme.get_tirps())
        elif args.command == "query":
            if not (
                util.is_valid_date(args.start_time)
                or (not args.end_time and util.is_valid_date(args.end_time))
            ):
                console.log(
                    "[bold red]Error: Please use the correct time format ![/bold red]"
                )
                exit()

            if args.end_time:
                console.log(testme.query_record(args.start_time, args.end_time))
            else:
                console.log(testme.query_record(args.start_time))

    else:
        console.log("[bold red]Fail to login[/bold red]")
        console.log(testme.login)
