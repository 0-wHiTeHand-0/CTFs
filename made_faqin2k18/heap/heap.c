#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <sys/types.h>
void win();

struct internet {
    int priority;
    char *name;
};

char k[] = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";

void win(){
    char lol[] = "wV8E8u7OmgOS0WldXPoHWJDSaAP/gdRJ";
    char temp;
    int i = 0;
    int j = strlen(k)-1;
    int z = strlen(lol)-1;
    if (j != z){
        printf("Nope nope nope...\n");
        exit(1);
    }
    while (i<j){
        lol[i] = k[i] ^ 'a';
        temp = k[i];
        k[i] = k[j]-10 ;
        k[j] = temp-7 ;
        i++;
        j--;
    }
    printf("WINNER!!!\nfaq1n{%s}\n", k);
    exit(0);
}

int main(int argc, char **argv)
{
    if (argc != 3){
        printf("Syntax: ./test arg1 arg2\n");
        exit(1);
    }
    struct internet *i1, *i2, *i3;

    i1 = malloc(sizeof(struct internet));
    i1->priority = 1;
    i1->name = malloc(8);

    i2 = malloc(sizeof(struct internet));
    i2->priority = 2;
    i2->name = malloc(8);

    strcpy(i1->name, argv[1]);
    strcpy(i2->name, argv[2]);

    char lel[] = "KiBnIG8gYSB0IHMgZSB4ICogZyBvIGEgdCBzIGUgeCAqIGcgbyBhIHQgcyBlIHggKgpnICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBnCm8gLyAgICAgXCAgICAgICAgICAgICBcICAgICAgICAgICAgLyAgICBcICAgICAgIG8KYXwgICAgICAgfCAgICAgICAgICAgICBcICAgICAgICAgIHwgICAgICB8ICAgICAgYQp0fCAgICAgICBgLiAgICAgICAgICAgICB8ICAgICAgICAgfCAgICAgICA6ICAgICB0CnNgICAgICAgICB8ICAgICAgICAgICAgIHwgICAgICAgIFx8ICAgICAgIHwgICAgIHMKZSBcICAgICAgIHwgLyAgICAgICAvICBcXFwgICAtLV9fIFxcICAgICAgIDogICAgZQp4ICBcICAgICAgXC8gICBfLS1+fiAgICAgICAgICB+LS1fX3wgXCAgICAgfCAgICB4CiogICBcICAgICAgXF8tfiAgICAgICAgICAgICAgICAgICAgfi1fXCAgICB8ICAgICoKZyAgICBcXyAgICAgXCAgICAgICAgXy4tLS0tLS0tLS5fX19fX19cfCAgIHwgICAgZwpvICAgICAgXCAgICAgXF9fX19fXy8vIF8gX19fIF8gKF8oX18+ICBcICAgfCAgICBvCmEgICAgICAgXCAgIC4gIEMgX19fKSAgX19fX19fIChfKF9fX18+ICB8ICAvICAgIGEKdCAgICAgICAvXCB8ICAgQyBfX19fKS8gICAgICBcIChfX19fXz4gIHxfLyAgICAgdApzICAgICAgLyAvXHwgICBDX19fX18pICAgICAgIHwgIChfX18+ICAgLyAgXCAgICBzCmUgICAgIHwgICAoICAgX0NfX19fXylcX19fX19fLyAgLy8gXy8gLyAgICAgXCAgIGUKeCAgICAgfCAgICBcICB8X18gICBcXF9fX19fX19fXy8vIChfXy8gICAgICAgfCAgeAoqICAgIHwgXCAgICBcX19fXykgICBgLS0tLSAgIC0tJyAgICAgICAgICAgICB8ICAqCmcgICAgfCAgXF8gICAgICAgICAgX19fXCAgICAgICAvXyAgICAgICAgICBfLyB8IGcKbyAgIHwgICAgICAgICAgICAgIC8gICAgfCAgICAgfCAgXCAgICAgICAgICAgIHwgbwphICAgfCAgICAgICAgICAgICB8ICAgIC8gICAgICAgXCAgXCAgICAgICAgICAgfCBhCnQgICB8ICAgICAgICAgIC8gLyAgICB8ICAgICAgICAgfCAgXCAgICAgICAgICAgfHQKcyAgIHwgICAgICAgICAvIC8gICAgICBcX18vXF9fXy8gICAgfCAgICAgICAgICB8cwplICB8ICAgICAgICAgICAvICAgICAgICB8ICAgIHwgICAgICAgfCAgICAgICAgIHxlCnggIHwgICAgICAgICAgfCAgICAgICAgIHwgICAgfCAgICAgICB8ICAgICAgICAgfHgKKiBnIG8gYSB0IHMgZSB4ICogZyBvIGEgdCBzIGUgeCAqIGcgbyBhIHQgcyBlIHggKgo=";
    printf("It's a trap!!!\n");
}
