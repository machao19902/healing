from datetime import datetime

from st2common.runners.base_action import Action

class CounterAction(Action):

    # append content into file
    def run(self, cmd, count):
        fileName = "/home/counter.txt"
        try:
            currTime = str(datetime.now())
            # note, a+ means append instead of w+
            with open(fileName, "a+") as fr:
                realContent = "healing, count: " + str(count) + ", cmd: "  + str(cmd) + ", time: " + currTime + "\n"
                fr.write(realContent)
            info = "count: {count}, cmd: {cmd}, time: {time}".format(
                count=count,
                cmd=cmd,
                time=currTime
            )
            print info
            return (True, cmd)
        except Exception as ex:
            info = "write count: {count}, cmd : {cmd}, exception: {exp}, message: {mes}".format(
                count=count,
                cmd=cmd,
                exp=ex.__class__.__name__,
                mes=ex
            )
            print info
            return (False, cmd)
