import sys
import importlib
from exceptions import TaskError,InvalidTaskNumberError,TaskNotFoundError

def main():

    WELCOME_MSG="Welcome to PyTask"


    task=sys.argv[1] if len(sys.argv) > 1 else None

    if not task:
        print(WELCOME_MSG)
        return


    try:
        module=importlib.import_module(f"plugins.{task}")
        arguments=sys.argv[2:]
        module.execute(arguments)

    except ModuleNotFoundError:
        print("Unknown Command")

    except TaskError as e:
        print(e)

    except Exception as e:
        print(e)


    
if __name__=="__main__":
    main()
