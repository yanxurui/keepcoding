// If a.c can not be changed and we still want to use structure definition in it, 
// we have to duplicate a definition in multiple source files

typedef struct {
    char *name;
    int age;
} S;

void func(S *s);

int main(int argc, char const *argv[])
{
    S s;
    s.name = "jobs";
    s.age = 25;
    func(&s);
    return 0;
}
