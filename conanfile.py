from conans import ConanFile, CMake, tools


class LoggerConan(ConanFile):
    name = "logger"
    version = "0.0.1"
    license = "<Put the package license here>"
    author = "dmitriy d.arbitman@gmail.com"
    url = "https://github.com/darbitman/logger"
    description = "cmake install/conan example of a logging library"
    topics = ("conan", "package")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": False}
    generators = "cmake"
    exports_sources = "./*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def _configure_cmake(self):
        cmake = CMake(self, cmake_program="cmake")
        cmake.configure(source_folder=".")
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["logger"]
