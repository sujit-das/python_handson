import os
#import overall_std_output as std

def check_path_exists(path):
    """
    Verifies if the path exists
    @param path: path to be verified
    @return (Check Result, Error message)
    """
    #std.add_overall_output("Checking existence of {}".format(path))
    if os.path.exists(path):
        print "OK", ""
    else:
        print "NOK", "The path {} does not exist or it is unreachable".format(path)

if __name__ == "__main__":
    check_path_exists("/home/sujitdas/log")
