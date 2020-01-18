#!/usr/bin/env python
# encoding: utf-8

import jenkins
import sys
import os

start_str = "added a comment."
end_str = "CONPHERENCE DETAIL"


def GetJulyTalkInfo(context_all):
    start_index = context_all.find(start_str) + len(start_str) + 2
    end_index = context_all.find(end_str) - 3
    return context_all[start_index:end_index]


def TriggerSendMail(list, cc, title_path, context_path):
    server = jenkins.Jenkins('http://10.75.8.176:8080/', username='hulingnan', password='ttcs')
    para = {}
    para["LIST"] = list

    if cc!="no":
        para["CC"] = cc

    para["TITLE"] = "there is no title"
    para["CONTEXT"] = "there is no context"

    if os.path.exists(title_path) and os.path.exists(context_path):
        title_file = open(title_path)
        context_file = open(context_path)
        para["CONTEXT"] = context_file.read()
        para["TITLE"] = title_file.read()
        if "july_talk" in para["TITLE"] or "mars_talk" in para["TITLE"]:
            para["TITLE"] = "[july_talk] " + GetJulyTalkInfo(para["CONTEXT"])
        para["TITLE"] = "[Phabricator] " + para["TITLE"]
        os.remove(title_path)
        os.remove(context_path)

    server.build_job('Phabricator', para)

if __name__ == '__main__':
    TriggerSendMail(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
