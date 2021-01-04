import setuptools

setuptools.setup(
    name="{{package_name}}",
    description="{{package_description}}",
    version="{{package_version}}",
    packages=setuptools.find_packages(),
    install_requires=[
        {% for package in required_packages %}
        "{{package}}",
        {% endfor %}
    ],
    entry_points={
        "console_scripts": [
            "{{package_name}}={{package_name}}.cli.__main__:main"
        ]
    }
)
