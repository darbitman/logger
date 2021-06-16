#include "Logger.hpp"

#include <iostream>

Logger::Logger(int line) : m_line(line) {}

void Logger::logit(std::string_view filename, std::string_view msg) {
  std::cout << filename << ':' << m_line << ' ' << msg << std::endl;
}
