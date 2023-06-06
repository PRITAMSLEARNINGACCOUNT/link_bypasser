import PyBypass
print("This programme can bypass shortner links and new gdtot links")
url = input("Enter Your URL???\n")
hello = url.split("/")
if hello[2] == "new7.gdtot.cfd":
    bypassed_link = PyBypass.bypass(
        f"{url}", gdtot_crypt="dlNPbnNRd3hVUHNqTzFUQ0puSDRnd1FhRXNGUVZ6ZlpYejVMdmY1ZTRrST0%3D")
    print(f"This is your bypassed link = {bypassed_link}")
else:
    try:
        bypassed_link = PyBypass.bypass(f"{url}")
        print(f"This is your bypassed link = {bypassed_link}")
    except Exception as e:
        print(e)
