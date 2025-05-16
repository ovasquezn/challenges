"""
2981. Find Longest Special Substring That Occurs Thrice I (Medium)

You are given a string s that consists of lowercase English letters.

A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.

Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.

A substring is a contiguous non-empty sequence of characters within a string.

Example 1:

Input: s = "aaaa"
Output: 2
Explanation: The longest special substring which occurs thrice is "aa": substrings "aaaa", "aaaa", and "aaaa".
It can be shown that the maximum length achievable is 2.
Example 2:

Input: s = "abcdef"
Output: -1
Explanation: There exists no special substring which occurs at least thrice. Hence return -1.
Example 3:

Input: s = "abcaba"
Output: 1
Explanation: The longest special substring which occurs thrice is "a": substrings "abcaba", "abcaba", and "abcaba".
It can be shown that the maximum length achievable is 1.

Constraints:

3 <= s.length <= 50
s consists of only lowercase English letters.
"""

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        
        # Comenzar desde la longitud más larga y verificar todas las subcadenas especiales
        for length in range(n, 0, -1):  # Longitudes desde n hasta 1
            # Generar todas las subcadenas posibles con la longitud actual
            for i in range(n - length + 1):
                substring = s[i:i + length]
                
                # Verificar si la subcadena es especial
                if len(set(substring)) == 1:  # Un solo carácter
                    # Contar cuántas veces aparece la subcadena en s
                    count = 0
                    for j in range(n - length + 1):
                        if s[j:j + length] == substring:
                            count += 1
                    
                    # Si aparece al menos 3 veces, devolver la longitud
                    if count >= 3:
                        return length
        
        return -1
# Example usage
s = "aaaa"
sol = Solution()
print(sol.maximumLength(s))
# Output: 2

# Example usage
s = "abcdef"
sol = Solution()
print(sol.maximumLength(s))
# Output: -1

# Time complexity: O(N^3)
# Space complexity: O(1)
# Where N is the length of the input string s. The function is_special takes O(N) time to check if a substring is special, and the nested loops iterate over all possible substrings, resulting in a time complexity of O(N^3). The space complexity is O(1) since we only use a constant amount of extra space.


"""
Explcación:
Dado un string s que consiste en letras minúsculas del alfabeto inglés, queremos encontrar la longitud de la subcadena especial más larga que ocurre al menos tres veces en s. Una subcadena especial es una subcadena que consta de un solo carácter.

Para resolver este problema, podemos seguir los siguientes pasos:

Comenzar desde la longitud más larga posible y verificar todas las subcadenas especiales de esa longitud.
Para cada longitud, generar todas las subcadenas posibles de esa longitud en s.
Verificar si cada subcadena es especial (es decir, consta de un solo carácter).
Contar cuántas veces aparece la subcadena en s.
Si la subcadena aparece al menos tres veces, devolver su longitud.
Si no se encuentra ninguna subcadena especial que aparezca al menos tres veces, devolver -1.
Este enfoque garantiza que encontremos la subcadena especial más larga que ocurre al menos tres veces en s. Al iterar sobre todas las longitudes posibles y todas las subcadenas de cada longitud, podemos encontrar la respuesta correcta.
"""