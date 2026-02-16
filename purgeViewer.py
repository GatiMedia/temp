def delete_all_viewers():
    deleted_nodes = []

    def find_and_delete(container):
        for n in container.nodes():
            if n.Class() == "Viewer":
                deleted_nodes.append(n.fullName())
                nuke.delete(n)
            elif isinstance(n, nuke.Group):
                find_and_delete(n)

    find_and_delete(nuke.root())

    if deleted_nodes:
        deleted_nodes_num=(f"Total nodes removed: {len(deleted_nodes)}")
        deleted_nodes=str('\n'.join(deleted_nodes))
        nuke.message(f"<font color=orange><center><h3>Deleted the following Viewer nodes:\n\n<font color=aqua>{deleted_nodes}\n\n<font color=orange>{deleted_nodes_num}")
    else:
        nuke.message("<font color=aqua><center><h3>No Viewer nodes found.")
