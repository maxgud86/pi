def pi(x,y,z):
        t = 0
        ans_array = []
        while t < 10000:
            temp_x = (4.0/(x*y*z))
            x = z
            y = y + 2
            z = z + 2
            temp_y = -(4.0/(x*y*z))
            x = z
            y = y + 2
            z = z + 2
            t = t + 1

            ans_array.append(temp_x)
            ans_array.append(temp_y)
        result = sum(ans_array) + 3.0
        return result

print (pi(2,3,4))
