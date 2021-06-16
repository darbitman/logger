#include "logger/log.hpp"

#include "Logger.hpp"

void logit(int line, const char* filename, const char* msg) { Logger(line).logit(filename, msg); }
