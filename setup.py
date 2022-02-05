import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="tinyman-py-sdk-old",
    description="Tinyman Python SDK",
    author="Tinyman",
    author_email="hello@tinyman.org",
    version="0.0.4",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    project_urls={
        "Source": "https://github.com/lrnz-vtl/tinyman-py-sdk-old",
    },
    install_requires=["py-algorand-sdk >= 1.6.0"],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    package_data={'tinyman-old.v1': ['asc.json']},
    include_package_data=True,
)
