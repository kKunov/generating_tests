import sys


def get_imports(readed_file):
    imports = []

    for line in readed_file:

        if line.startswith('import') or line.startswith('from'):
            imports.append(line)

    imports.append('import unittest')

    return imports


def get_test_prename(readed_file):
    for line in readed_file:

        if line.startswith('"This is a test class for testing'
                           ) and line.endswith('funciton"'):

            line = line.split()
            last_word = ''

            for word in line:

                if last_word == 'testing':
                    return word

                else:
                    last_word = word


def make_class_name(test):
    test = test.split('_')
    class_name = ''

    for word in test:
        class_name += word.title()

    class_name = 'class %sTest(unittest.TestCase):' % (class_name)

    return class_name


def prepare_test(line):
    text = ''

    test_part = []
    txt = True

    for word in line.split():

        if word == '->':
            txt = False

        elif txt is True:
            text += ' %s' % word

        else:
            test_part.append(word)

    test = ''

    if 'True' == test_part[2]:
        test += '        self.assertTrue(%s, %s)' % (test_part[0], text)

    elif 'False' == test_part[2]:
        test += '        self.assertFalse(%s, %s)' % (test_part[0], text)

    else:
        test += '        self.assertEqual(%s, %s, %s)' % (test_part[0],
                                                          test_part[1], text)

    return test


def take_test_lines(readed_file):
    test_lines = []

    for line in readed_file:

        if '->' in line:
            test_lines.append(line)

    return test_lines


def make_tests(readed_file):
    test_lines = take_test_lines(readed_file)
    tests = []

    for line in test_lines:
        tests.append(prepare_test(line))

    return tests


def main():
    file_name = sys.argv[1]

    file = open(file_name, 'r')
    readed_file = file.read().split('\n')
    file.close()

    imports = get_imports(readed_file)
    test_prename = get_test_prename(readed_file)
    class_name = make_class_name(test_prename)
    tests = make_tests(readed_file)
    magic_if = "if __name__ == '__main__':\n    unittest.main()"

    new_file_name = ''

    for index in range(len(file_name)):

        if file_name[index] != '.':
            new_file_name += file_name[index]

        else:
            new_file_name += '.py'
            break

    file = open(new_file_name, 'w')

    for line in imports:
        file.write("%s\n\n" % line)

    file.write("\n%s\n" % class_name)

    for index, line in enumerate(tests):
        file.write('    def testCase%s(self):\n' % (index + 1))
        file.write("%s\n\n" % line)

    file.write('\n%s\n' % magic_if)
    file.close()

if __name__ == '__main__':
    main()
