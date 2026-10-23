char* longestCommonPrefix(char** strs, int strsSize) {
    int len=strlen(strs[0]);
    char* s=malloc((len+1)*sizeof(char));
    int i=0,j;
    
    while(strs[0][i]!='\0'){
        for(j=1;j<strsSize;j++){
            if(strs[j][i]!=strs[0][i]){
                break;
            }

        }
        if(j<strsSize){
            break;
        }
        s[i]=strs[0][i];
        i++;
    }
    s[i]='\0';
    return s;
   
   
    
}