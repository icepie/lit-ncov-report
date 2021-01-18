import argparse
from litncov.user import litUesr
from rich.console import Console

def main():
    console = Console()

    parser = argparse.ArgumentParser(description="A ncov cli tool for LIT(Luoyang Institute of Science and Technology)")
    parser.add_argument("-u", "--username", help="the username", required=True)
    parser.add_argument("-p", "--password", help="the password", required=True)

    subparsers = parser.add_subparsers(dest="command")
    report = subparsers.add_parser("report", help="run the report action")
    report.add_argument("-r", "--rtimes", help="the report times {1,2,3}")

    # info = subparsers.add_parser("info", help="get the user info")

    # query = subparsers.add_parser("query", help="query history of the user report")

    args = parser.parse_args()

    testme = litUesr(args.username, args.password)
    if args.command == "report":
        if testme.is_logged:
            console.log("登陆成功")
            if not testme.is_record_today(1):
                console.log(testme.first_record(mode='last', rtimes=3))
            else:
                console.log("今天已完成上报了哦")
        else:
                console.log("登陆失败", style="bold red")