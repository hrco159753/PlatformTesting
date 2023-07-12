from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps

import pathlib
import os

class SystemRecipe(ConanFile):
    name = "system"
    version = "0.0.1"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*"

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        pass

    def layout(self):
        cmake_layout(self)

        self.cpp.source.includedirs = []

        build_path = pathlib.Path(os.path.join(self.recipe_folder, self.folders.build))
        self.cpp.build.objects = list(build_path.rglob("*.obj"))
        self.cpp.build.bindirs = []
        self.cpp.build.libdirs = []

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.user_presets_path = False
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        package_bin_path = pathlib.Path(self.package_folder, 'bin')
    
        self.cpp_info.libdirs = []
        self.cpp_info.bindirs = []
        self.cpp_info.includedirs = []
        self.cpp_info.objects = list(package_bin_path.rglob("*.obj"))
    

