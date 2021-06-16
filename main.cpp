#include "logger/log.hpp"

int main() {
  logit(__LINE__, __FILE__, "Hello, World!\n");
  return 0;
}
