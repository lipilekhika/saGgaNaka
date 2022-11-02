from time import sleep
from git import GIT_OK
import shubhlipi as sh
from getpass import getpass
import os
from dotenv import load_dotenv

load_dotenv()
# Refer https://docs.github.com/en/rest/reference/releases


def get_git_key():
    global GIT_KEY, KEY
    if GIT_KEY == "":
        key = getpass("key = ") if KEY == "" else KEY
        a = sh.post(f'{sh.env("link")}/api/git_key', json={"key": sh.from_base64(key)})
        res = a.json()
        if a.status_code != 200:
            print(res["detail"])
            exit()
        GIT_KEY = res["value"]
    return GIT_KEY


root = sh.env("sthAnam")
GIT_KEY = ""
KEY = ""
if "KEY" in os.environ:
    KEY = os.environ["KEY"]
f = [
    {
        "file": root + r"\bin\Lipi Lekhika Installer.zip",
        "tag": "v" + sh.env("pc_ver"),
        "repo": "lipilekhika/saGgaNaka",
        "more": f'scp "{root}\\bin\\Lipi Lekhika Installer.zip" lipilekhika@frs.sourceforge.net:/home/frs/project/lipilekhika',
    },
    {
        "file": root + r"\bin\Lipi Lekhika Portable.exe",
        "tag": "v" + sh.env("pc_ver"),
        "repo": "lipilekhika/saGgaNaka",
    },
    {
        "file": root + r"\bin\Lipi Lekhika.apk",
        "tag": "v" + sh.env("android_ver"),
        "repo": "lipilekhika/jAlAnuprayog",
        "more": f'scp "{root}\\bin\\Lipi Lekhika.apk" lipilekhika@frs.sourceforge.net:/home/frs/project/lipilekhika',
    },
]

if sh.args(0) == "release":
    for x in sh.argv[1:]:
        try:
            d = f[int(x) - 1]
        except:
            exit()
        if "more" in d and "s" in sh.argv:
            print("Enter for Source Forge Upload of :-", d["file"].split("\\")[-1])
            sh.cmd(d["more"], file=True)
        sh.upload_release_file(d["file"], d["repo"], d["tag"], get_git_key())
elif sh.args(0) == "kAraH":
    tag = sh.argv[2]
    link = f[int(sh.argv[1]) - 1]["repo"]
    if input(f"do you want to create new release {tag} in {link}? ") != "astu":
        exit()
    sh.make_release_tag(link, tag, get_git_key())
elif sh.args(0) == "delete":
    tag = sh.argv[2]
    link = f[int(sh.argv[1]) - 1]["repo"]
    if input(f"do you want delete release {tag} from {link}? ") != "astu":
        exit()
    sh.delete_release_tag(link, tag, get_git_key())
elif sh.args(0) == "delete_kAraH":
    tag = sh.argv[2]
    link = f[int(sh.argv[1]) - 1]["repo"]
    if input(f"do you want delete release {tag} from {link}? ") != "astu":
        exit()
    sh.delete_release_tag(link, tag, get_git_key())
    sh.make_release_tag(link, tag, get_git_key())
elif sh.args(0) == "tracker":
    if input("Are you sure to update tracking files ? ") != "astu":
        exit()
    datt = {
        "jala": [".js", "application/javascript", 0, "जालस्थानस्य"],
        "ext": [".js", "application/javascript", 0, "अन्यानाम्"],
        "sang": [".txt", "text/plain", 0, "सङ्गणकस्य"],
        "sang_bhasha": [".txt", "text/plain", 1, "सङ्गणकभाषायाः"],
        "bhasha": [".js", "application/javascript", 1, "जालभाषायाः"],
    }
    lst = [["su"] + list(sh.script_list.values()), list(sh.lang_list.values())]
    link = "lipilekhika/dist"
    get_git_key()

    def mk(x):
        v = datt[x]
        sh.delete_release_tag(link, x, get_git_key(), log=False)
        sh.make_release_tag(link, x, get_git_key(), log=False, name=v[3])
        sleep(1)
        th = []
        for y in lst[v[2]]:
            th.append(
                sh.start_thread(
                    lambda: sh.upload_release_file(
                        y + v[0],
                        link,
                        x,
                        get_git_key(),
                        fl_type=v[1],
                        fl_data=" ",
                        log=False,
                    )
                )
            )
        for y in th:
            y.join()

    thrds = []
    tm = sh.time()
    for x in datt:
        thrds.append(sh.start_thread(lambda: mk(x)))
    for x in thrds:
        x.join()
    print("Added Tracking Files", sh.time() - tm)
