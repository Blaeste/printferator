"""Tests pour ft_printf"""

TESTS = [
    ("printf/basic_char", '''
#include <stdio.h>
int main() {
    int result1 = printf("Hello %c", 'A');
    printf("\\n");
    int result2 = ft_printf("Hello %c", 'A');
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/basic_string", '''
#include <stdio.h>
int main() {
    int result1 = printf("Hello %s", "world");
    printf("\\n");
    int result2 = ft_printf("Hello %s", "world");
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/basic_int", '''
#include <stdio.h>
int main() {
    int result1 = printf("Number: %d", 42);
    printf("\\n");
    int result2 = ft_printf("Number: %d", 42);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/basic_int_negative", '''
#include <stdio.h>
int main() {
    int result1 = printf("Number: %d", -42);
    printf("\\n");
    int result2 = ft_printf("Number: %d", -42);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/hex_lowercase", '''
#include <stdio.h>
int main() {
    int result1 = printf("Hex: %x", 255);
    printf("\\n");
    int result2 = ft_printf("Hex: %x", 255);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/hex_uppercase", '''
#include <stdio.h>
int main() {
    int result1 = printf("Hex: %X", 255);
    printf("\\n");
    int result2 = ft_printf("Hex: %X", 255);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/unsigned", '''
#include <stdio.h>
int main() {
    int result1 = printf("Unsigned: %u", 4294967295U);
    printf("\\n");
    int result2 = ft_printf("Unsigned: %u", 4294967295U);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/pointer", '''
#include <stdio.h>
int main() {
    int x = 42;
    int result1 = printf("Pointer: %p", &x);
    printf("\\n");
    int result2 = ft_printf("Pointer: %p", &x);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/percent", '''
#include <stdio.h>
int main() {
    int result1 = printf("Percent: %%");
    printf("\\n");
    int result2 = ft_printf("Percent: %%");
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/mixed", '''
#include <stdio.h>
int main() {
    int result1 = printf("Mixed: %c %s %d %x", 'A', "test", 42, 255);
    printf("\\n");
    int result2 = ft_printf("Mixed: %c %s %d %x", 'A', "test", 42, 255);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/null_string", '''
#include <stdio.h>
int main() {
    int result1 = printf("Null: %s", (char*)0);
    printf("\\n");
    int result2 = ft_printf("Null: %s", (char*)0);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/zero", '''
#include <stdio.h>
int main() {
    int result1 = printf("Zero: %d", 0);
    printf("\\n");
    int result2 = ft_printf("Zero: %d", 0);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    # ===============================
    # 🔥 EDGE CASES - Tests avancés
    # ===============================

    ("printf/edge_int_max", '''
#include <stdio.h>
#include <limits.h>
int main() {
    int result1 = printf("INT_MAX: %d", INT_MAX);
    printf("\\n");
    int result2 = ft_printf("INT_MAX: %d", INT_MAX);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/edge_int_min", '''
#include <stdio.h>
#include <limits.h>
int main() {
    int result1 = printf("INT_MIN: %d", INT_MIN);
    printf("\\n");
    int result2 = ft_printf("INT_MIN: %d", INT_MIN);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/edge_uint_max", '''
#include <stdio.h>
#include <limits.h>
int main() {
    int result1 = printf("UINT_MAX: %u", UINT_MAX);
    printf("\\n");
    int result2 = ft_printf("UINT_MAX: %u", UINT_MAX);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/edge_hex_zero", '''
#include <stdio.h>
int main() {
    int result1 = printf("Hex zero: %x", 0);
    printf("\\n");
    int result2 = ft_printf("Hex zero: %x", 0);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/edge_hex_max", '''
#include <stdio.h>
#include <limits.h>
int main() {
    int result1 = printf("Hex max: %x", UINT_MAX);
    printf("\\n");
    int result2 = ft_printf("Hex max: %x", UINT_MAX);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/edge_char_null", '''
#include <stdio.h>
int main() {
    int result1 = printf("Char null: %c", '\\0');
    printf("\\n");
    int result2 = ft_printf("Char null: %c", '\\0');
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/edge_char_special", '''
#include <stdio.h>
int main() {
    int result1 = printf("Special: %c%c%c", '\\t', '\\n', '\\r');
    int result2 = ft_printf("Special: %c%c%c", '\\t', '\\n', '\\r');

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/edge_string_empty", '''
#include <stdio.h>
int main() {
    int result1 = printf("Empty: '%s'", "");
    printf("\\n");
    int result2 = ft_printf("Empty: '%s'", "");
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/edge_string_long", '''
#include <stdio.h>
int main() {
    char *long_str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.";
    int result1 = printf("Long: %s", long_str);
    printf("\\n");
    int result2 = ft_printf("Long: %s", long_str);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/edge_pointer_null", '''
#include <stdio.h>
int main() {
    int result1 = printf("Null ptr: %p", (void*)0);
    printf("\\n");
    int result2 = ft_printf("Null ptr: %p", (void*)0);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/edge_multiple_percent", '''
#include <stdio.h>
int main() {
    int result1 = printf("Multiple: %%%% = %%");
    printf("\\n");
    int result2 = ft_printf("Multiple: %%%% = %%");
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/edge_no_args", '''
#include <stdio.h>
int main() {
    int result1 = printf("No args at all");
    printf("\\n");
    int result2 = ft_printf("No args at all");
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/edge_mixed_complex", '''
#include <stdio.h>
int main() {
    int result1 = printf("Complex: %c|%s|%d|%i|%u|%x|%X|%p|%%", 'Z', "test", -123, 456, 789U, 0xABC, 0xDEF, &result1);
    printf("\\n");
    int result2 = ft_printf("Complex: %c|%s|%d|%i|%u|%x|%X|%p|%%", 'Z', "test", -123, 456, 789U, 0xABC, 0xDEF, &result2);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/edge_many_args", '''
#include <stdio.h>
int main() {
    int result1 = printf("%d %d %d %d %d %d %d %d %d %d", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
    printf("\\n");
    int result2 = ft_printf("%d %d %d %d %d %d %d %d %d %d", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/edge_hex_lowercase_all", '''
#include <stdio.h>
int main() {
    int result1 = printf("Hex: %x %x %x", 0xabcdef, 0x123456, 0x789abc);
    printf("\\n");
    int result2 = ft_printf("Hex: %x %x %x", 0xabcdef, 0x123456, 0x789abc);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/edge_hex_uppercase_all", '''
#include <stdio.h>
int main() {
    int result1 = printf("HEX: %X %X %X", 0xabcdef, 0x123456, 0x789abc);
    printf("\\n");
    int result2 = ft_printf("HEX: %X %X %X", 0xabcdef, 0x123456, 0x789abc);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/edge_signed_vs_unsigned", '''
#include <stdio.h>
int main() {
    int neg = -1;
    int result1 = printf("Signed: %d, Unsigned: %u", neg, neg);
    printf("\\n");
    int result2 = ft_printf("Signed: %d, Unsigned: %u", neg, neg);
    printf("\\n");

    if (result1 != result2) return 1;
    return 0;
}'''),

    ("printf/edge_return_value_check", '''
#include <stdio.h>
int main() {
    int r1 = printf("Test return value");
    int r2 = ft_printf("Test return value");

    if (r1 != r2) return 1;
    if (r1 != 17) return 1;  // "Test return value" = 17 chars
    return 0;
}'''),
]
