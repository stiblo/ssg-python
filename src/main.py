from copystatic import copy_static_to_public

static_dir_path = "./static"
public_dir_path = "./public"


def main():
    print(f"Copying static files to public directory ...")
    copy_static_to_public(static_dir_path,public_dir_path)

main()

