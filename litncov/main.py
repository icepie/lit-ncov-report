import argparse
from litncov.user import litUesr
from rich.console import Console


def main():
    console = Console()

    parser = argparse.ArgumentParser(
        description="A ncov cli tool for LIT(Luoyang Institute of Science and Technology)",
        epilog="(c) 2020 icepie.dev@gmail.com",
    )
    parser.add_argument("-u", "--username", help="the username", required=True)
    parser.add_argument("-p", "--password", help="the password", required=True)

    subparsers = parser.add_subparsers(dest="command")
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
    info = subparsers.add_parser("info", help="get the user info")
    info.add_argument(
        "-f", "--family", action="store_true", help="the user family info"
    )
    info.add_argument(
        "-l", "--last_record", action="store_true", help="the user last record info"
    )
    query = subparsers.add_parser("query", help="query history of the user report")
    query.add_argument("-s", "--startime", help="the start time of the report history")
    query.add_argument(
        "-e", "--endtime", help="the end time of the report history, default today"
    )

    args = parser.parse_args()

    # check the command
    if not args.command or args.command not in {"report", "info", "query"}:
        parser.print_help()
        exit()

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

    testme = litUesr(args.username, args.password)
    if args.command == "report":
        if testme.is_logged:
            console.log("[bold cyan]Login successful[/bold cyan]")
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
        else:
            console.log("[bold red]Fail to login[/bold red]")
            console.log(testme.login)
