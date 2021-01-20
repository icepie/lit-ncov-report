import argparse
from litncov.user import litUesr
from rich.console import Console

def main():
    console = Console()

    parser = argparse.ArgumentParser(description="A ncov cli tool for LIT(Luoyang Institute of Science and Technology)", epilog='(c) 2020 icepie.dev@gmail.com')
    parser.add_argument("-u", "--username", help="the username", required=True)
    parser.add_argument("-p", "--password", help="the password", required=True)

    subparsers = parser.add_subparsers(dest="command")
    report = subparsers.add_parser("report", help="run the report action")
    report.add_argument("-a", "--all", action='store_true', help="do the all report tasks today")
    report.add_argument("-f", "--force", action='store_true', help="forcely report")
    report.add_argument("-r", "--rtime", help="the report time {1,2,3}")
    report.add_argument("-m", "--mode", help="the report mode {last,random,manual}")
    report.add_argument("-t", "--temp", help="the body temperature (float)")
    # info = subparsers.add_parser("info", help="get the user info")

    # query = subparsers.add_parser("query", help="query history of the user report")

    args = parser.parse_args()

    # check the command
    if not args.command or args.command not in {'report', 'info', 'query'}:
        parser.print_help()
        exit()

    # check rtime arg
    if args.rtime and args.rtime not in {1, 2, 3}:
        parser.print_help()
        exit()
    
    # check mode arg
    if args.rtime and args.rtime not in {'last','random','manual'}:
        parser.print_help()
        exit()

    # check temp arg
    if args.temp and (float(args.temp) >= 37.3 or float(args.temp) < 35.0)   :
        console.log("[bold red]Dangerous body temperature[/bold red]")
        console.log("[bold red]If this is your body temperature is too high or low, plz use the [u]-f[/u] parameter to report[/bold red]")
        exit()

    testme = litUesr(args.username, args.password)
    if args.command == "report":
        if testme.is_logged:
            console.log("[bold cyan]Login successful[/bold cyan]")
            # start report
            if not testme.is_record_today(1) or args.force:
                console.log(testme.first_record(mode='last', rtimes=3))
            else:
                console.log("You have finished reporting today")
        else:
                console.log("[bold red]Fail to login[/bold red]")
                console.log(testme.login)


if __name__ == "__main__":
    main()