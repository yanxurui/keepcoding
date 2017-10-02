// If a.c can not be changed and we still want to use structure definition in it, 
// we have to duplicate a definition in multiple source files
struct S {
	char *name;
	int age;
};

void func(int age);

int main(int argc, char const *argv[])
{
	struct  S s;
	s.name = "jobs";
	s.age = 25;
	func(s.age);
	return 0;
}
