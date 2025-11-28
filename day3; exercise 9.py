#Ask the user for a short message. Print it repeated three times.
import sys
message = input("Enter a short message: ") #tested with hello
def main():
    for i in range (3):
        print(message)
    return 0
if __name__ == '__main__':
    sys.exit(main())
