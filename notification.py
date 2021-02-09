import notify2, os

def notif_download_started():
    notify2.init("Starting Download")
    n = notify2.Notification(summary="Download started",message="Wait for a few seconds while file is being downloaded")
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.show() 

def notif_download_finished():
    notify2.init("Download fished")
    n = notify2.Notification(summary="Download finished",message="Your download is finished, enjoy the file")
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.show() 