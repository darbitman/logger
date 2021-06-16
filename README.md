# Logger is just a logging-library aimed at demonstrating how to configure CMake correctly and integrate with Conan
## Create a Conan package from local sources
```
mkdir build
```
then
```
cd build
```
Inside `build`
```
conan install ..
```
 to generate `conanbuildinfo.txt` which is required to build a package.

Finally 
```
conan export .. logger/0.0.1@darbitman/stable -f
```

Then the package can be consumed by others who want this logging framework.

To use the package, use the repo: https://github.com/darbitman/use_logger.git