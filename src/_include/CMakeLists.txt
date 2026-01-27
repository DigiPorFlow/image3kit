add_library(sirun_utils STATIC
    SiRun.cpp
)
target_include_directories(sirun_utils PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_compile_features(sirun_utils PUBLIC cxx_std_23)

add_executable(check_sirun test_sirun.cpp)
target_link_libraries(check_sirun PRIVATE sirun_utils)

add_executable(check_input test_input.cpp)
target_link_libraries(check_input PRIVATE sirun_utils)
