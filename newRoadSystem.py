def newRoadSystem(roadRegister):

    incoming = [sum(r) for r in roadRegister]
    outgoing = [sum(r) for r in zip(*roadRegister)]
    return all(i == o for i, o in zip(incoming, outgoing))
