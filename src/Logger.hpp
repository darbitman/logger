#pragma once

#include <string_view>

struct Logger {
  Logger(int line);
  void logit(std::string_view filename, std::string_view msg);

 private:
  int m_line = 0;
};
