from elements.element import Element


class FunctionCall(Element):
    """"
    HTML:
    <funcname>
        <param ... />
    </funcname>

    C: funcname(param1, param2, etc..)
    """

    def to_c(self):

        params = []
        # get params:
        for el in self.children:
            if el.tagname == "param":
                params.append(el.data.strip())

        return "{}({})\n".format(  # for example: multiply(4, 5)
            self.tagname,
            ", ".join([param for param in params])
        )
