last_week = ["hide", "seek", "tag"]
this_week = ["hide", "seek", "jump", "run"]
last_week=set(last_week)
this_week=set(this_week)
print(list(this_week-last_week))