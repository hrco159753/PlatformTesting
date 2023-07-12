cmake_minimum_required(VERSION 3.23)

project(System LANGUAGES ASM C)
enable_testing()

add_library(System OBJECT)
target_sources(System
	PRIVATE
		"src/gcc_startup_nrf52840.S"
		"src/system.c"
)

include(GNUInstallDirs)
install(TARGETS System
	OBJECTS DESTINATION ${CMAKE_INSTALL_BINDIR}
)
