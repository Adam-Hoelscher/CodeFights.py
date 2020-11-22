def financialCrisis(roadRegister):
    def gen():
        for k in range(len(roadRegister)):
            front = roadRegister[:k]
            back = roadRegister[k + 1:]
            all_rows = front + back
            for p, r in enumerate(all_rows):
                front = r[:k]
                back = r[k + 1:]
                all_rows[p] = front + back
            yield all_rows
            
    return list(gen())
