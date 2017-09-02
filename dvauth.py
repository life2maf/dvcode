def auth(k, login, pwd, db): #k - тип авторизации, 0 если регулярное выражение, 1 если лог-пасс, 2 - регистрация. db - путь к файлу, где все это хранится (должен представлять собой либо список строк либо разделенный список). Sce - тип (0 - логин, 1 - регистрация)
    text = []
    if k != 0:
        if k == 1:
            f = open(db)
            for line in f:
                l = line.split()
                try:
                    if l[0] == login:
                        if l[1] == pwd:
                            f.close()
                            return(1)

                        else:
                            f.close()
                            return(0)

                except LookupError:
                    f.close()
                    return(2)
            f.close()
        elif k == 2:
            f = open(db)
            for line in f:
                l = line.split()
                try:
                    if l[0] == login:
                        f.close()
                        return(1)

                except LookupError:
                    f.close()
                    return(2)
                text.append(line)
            f.close()
            f = open(db, 'w')
            for i in text:
                f.write(i+'\n')
            f.write(login + ' '+ pwd)
            f.close()
        else:
            return(2)
    else:
        f = open(db)
        for line in f:
            if line == db:
                return(0)
        f.close()
        return(1)
