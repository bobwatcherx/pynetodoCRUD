
import pynecone as pc



class State(pc.State):
    """The app state."""
    todo:list
    new_todo:str
    edit_my_todo:str
    id_edit:int
    open_dialog:bool = False

    def addnewtodo(self):
        # NOW ADD TO todo
        if not self.new_todo == "":
            self.todo.append(self.new_todo)
            print(self.todo)

            # AND CLEAR INPUT
            self.new_todo = ""


    def edit_todo(self,mytodo,index):
        # AND NOW FOR EDIT 
        # OPEN DIALOG EDIT FOR EDIT
        self.open_dialog = True
        self.id_edit = index
        self.edit_my_todo = mytodo


    def delete_todo(self,mytodo):
        # NOW LOOP AND FIND You click Todo if found then delete
        for x in self.todo:
            if x == mytodo:
                self.todo.remove(mytodo)
            else:
                print("You no data !!!")
    def closemodal(self):
        self.open_dialog = not (self.open_dialog)

    def saveinput(self):
        print("you saved")
        self.todo[self.id_edit] = self.edit_my_todo
        print(self.edit_my_todo)

        # AND CLEAR INPUT
        self.edit_my_todo = ""
        # AND CLOSE DIALOG
        self.open_dialog = False
 


def list_todos(mytodo,index):
    return pc.list(
        pc.list_item(
            pc.hstack(
                pc.text(mytodo,size=20),
                # INDEX IS YOU index of todo you input
                pc.text(index,size=20),
                # CREATE EDIT AND DELETE BUTTON
                pc.button("edit",
                    bg="blue",color="white",
                    on_click=lambda: State.edit_todo(mytodo,index)
                    ),
                 pc.button("delete",
                    bg="red",color="white",
                    on_click=lambda: State.delete_todo(mytodo)
                    ),
                )
            )
        )




def index() -> pc.Component:
    return pc.center(

        # NOW CREATE DIALOG EDIT
        pc.modal(
            pc.modal_overlay(
                pc.modal_content(
                    pc.modal_header("edit"),
                    pc.modal_body(
                        pc.input(
                            value=State.edit_my_todo,
                            on_change=State.set_edit_my_todo
                            )
                        ),
                    pc.modal_footer(
                        pc.button("close",
                            on_click=State.closemodal
                            ),
                        pc.button("save",
                            bg="green",color="white",
                            on_click=State.saveinput
                            ),
                        
                        )
                    )
                ),
            is_open = State.open_dialog,
            close_on_overlay_click=False

            ),


        pc.vstack(
            pc.input(
                on_change=State.set_new_todo,
                placeholder="new todo"
                ),
            pc.button("add new todo",
                bg="purple",
                color="white",
                on_click=State.addnewtodo
                ),
            # NOW FETCH ALL TODO HERE 
            # LOOP TODO HERE
            pc.foreach(State.todo,list_todos)
            )
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
