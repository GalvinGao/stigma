
from stigma import SmaliMethodDef
import sys

def type_safety_checker_test():
    
    method_text = '''.method public leakPasswd(Landroid/view/View;)V
    .locals 6
    .param p1, "v"    # Landroid/view/View;

    .line 181
    const v0, 0x7f070050

    invoke-virtual {p0, v0}, Ledu/fandm/enovak/leaks/Main;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/EditText;

    .line 182
    .local v0, "et":Landroid/widget/EditText;
    invoke-virtual {v0}, Landroid/widget/EditText;->getText()Landroid/text/Editable;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v1

    .line 184
    .local v1, "pass":Ljava/lang/String;
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "Leaked Password: "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-direct {p0, v2}, Ledu/fandm/enovak/leaks/Main;->prependToLog(Ljava/lang/String;)V

    .line 186
    new-instance v2, Ledu/fandm/enovak/leaks/Main$ServerLeakTask;

    invoke-direct {v2, p0}, Ledu/fandm/enovak/leaks/Main$ServerLeakTask;-><init>(Ledu/fandm/enovak/leaks/Main;)V

    .line 189
    .local v2, "slt":Ledu/fandm/enovak/leaks/Main$ServerLeakTask;
    const-string v3, "password"

    invoke-virtual {v1, v3}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v3

    const/4 v4, 0x0

    const/4 v5, 0x1

    if-eqz v3, :cond_0

    .line 190
    const-string v3, "a"

    .line 191
    .local v3, "coded":Ljava/lang/String;
    new-array v5, v5, [Ljava/lang/String;

    aput-object v3, v5, v4

    invoke-virtual {v2, v5}, Ledu/fandm/enovak/leaks/Main$ServerLeakTask;->execute([Ljava/lang/Object;)Landroid/os/AsyncTask;

    .line 192
    .end local v3    # "coded":Ljava/lang/String;
    goto :goto_0

    .line 193
    :cond_0
    new-array v3, v5, [Ljava/lang/String;

    aput-object v1, v3, v4

    invoke-virtual {v2, v3}, Ledu/fandm/enovak/leaks/Main$ServerLeakTask;->execute([Ljava/lang/Object;)Landroid/os/AsyncTask;

    .line 198
    :goto_0
    return-void
.end method'''

    method_text_static = '''.method public static leakPasswd()V
    .locals 1

    .line 181
    const v0, 0x7f070050

    return-void
.end method'''


    method_list = method_text.split("\n")
    smd =  SmaliMethodDef.SmaliMethodDef(method_list, None)
    
    for i in range(len(method_list)):
        print("line: " + str(method_list[i]), "\nline_map: ", smd.tcs.method_type_list[i])
    
    
    method_list_static = method_text_static.split("\n")
    smd1 = SmaliMethodDef.SmaliMethodDef(method_list_static, None)
    
    #smd1.tcs.type_query("v1", 4)
    #print(smd1.tcs.type_query("v0", 4))

if __name__=="__main__":
    type_safety_checker_test()