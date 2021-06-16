add_library(logger STATIC Logger.cpp Logger.hpp log.cpp)
add_library(Logger::logger ALIAS logger)
target_include_directories(logger PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}/include>
  $<INSTALL_INTERFACE:include>)

# create the library and use the INTERFACE libraries only for building
target_link_libraries(logger PRIVATE
                      $<BUILD_INTERFACE:project_options>
                      $<BUILD_INTERFACE:project_warnings>)

# install the config file which will be used to help find the package
install(FILES loggerConfig.cmake DESTINATION lib/cmake/logger)

# install the version config file to help find the correct version
include(CMakePackageConfigHelpers)
write_basic_package_version_file(loggerConfigVersion.cmake VERSION 0.0.1 COMPATIBILITY AnyNewerVersion)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/loggerConfigVersion.cmake DESTINATION lib/cmake/logger)

# install the headers and libs
install(TARGETS logger EXPORT loggerTargets
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib
        RUNTIME DESTINATION bin
        INCLUDES DESTINATION include)

# install the .cmake files that help find target names
install(EXPORT loggerTargets
        DESTINATION lib/cmake/logger
        FILE loggerTargets.cmake
        NAMESPACE Logger::)

# install the public headers
install(DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/include/"
        DESTINATION include
        FILES_MATCHING
        PATTERN "*.hpp")
