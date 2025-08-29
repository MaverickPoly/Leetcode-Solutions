import os
import shutil

targets = {
    "Python": ".py",
    "Go": ".go",
    "C": ".c",
    "C++": ".cpp",
    "Rust": ".rs"
    # "Dart": ".dart",
    # "PHP": ".php",
}

def main():
    print("Moving files...")
    extensions = list(targets.values())
    languages = list(targets.keys())

    total = {language: 0 for language, _ in targets.items()}

    entries = os.listdir(".")
    for entry in entries:
        if os.path.isfile(entry):
            root, extension = os.path.splitext(entry)

            if extension not in extensions:
                print(f"Extension {extension} not found!")
                continue

            index = extensions.index(extension)
            language = languages[index]
            destination = os.path.join(".", language, entry)

            source_dir = os.path.abspath(f"{entry}")
            dest_dir = os.path.abspath(destination)

            total[language] += 1

            try:
                shutil.move(source_dir, dest_dir)
            except Exception as e:
                print(f"{source_dir} - {dest_dir}")
                print(f"Failed to move file: {e}")

    print("\nFinal Result:")
    for language, count in total.items():
        print(f"- {language}: {count}")
    

if __name__ == "__main__":
    main()
