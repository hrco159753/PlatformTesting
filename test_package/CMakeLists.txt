cmake_minimum_required(VERSION 3.23)

project(PackageTest CXX)
enable_testing()

find_package(system CONFIG REQUIRED)

add_executable(example)
target_sources(example
	PRIVATE
		"src/example.cpp"
)

target_link_libraries(example PRIVATE system::system)
