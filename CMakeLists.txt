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

# find_package(logger 0.0.0 CONFIG REQUIRED HINTS /tmp/local/)

add_subdirectory(src)

add_executable(main main.cpp)
target_link_libraries(main PRIVATE Logger::logger
                      $<BUILD_INTERFACE:project_options>
                      $<BUILD_INTERFACE:project_warnings>)
