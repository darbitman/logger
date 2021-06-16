cmake_minimum_required(VERSION 3.10)

project(Logger VERSION 0.0.1 LANGUAGES CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS TRUE)

# Link this "library" to set the c++ standard/compile-time options
add_library(project_options INTERFACE)
target_compile_features(project_options INTERFACE cxx_std_17)

# Link this "library" to use warnings
add_library(project_warnings INTERFACE)
include(cmake/CompilerWarnings.cmake)
set_project_warnings(project_warnings)

add_subdirectory(src)
