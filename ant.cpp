using namespace std;
int a[4]{15, 26, 7, 1};
int size = 4;
for (int i = 0; i < size - 1; i++){
    temp = i;
    for (int j = 1; j < size - 1; j++){
        if mass[j] < mass[temp]{
            temp = j;
        }
    }
    mass[j] = mass[temp];
    mass[j] = mass[i];
    mass[i] = mass[temp];
}
for (int i =0; i < size-1; i++){
    cout << mass[i] << endl;
}
system("pause")