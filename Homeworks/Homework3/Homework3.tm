<TeXmacs|2.1.2>

<style|generic>

<\body>
  <\hide-preamble>
    \;

    <assign||<macro|body|<\question>
      <arg|body>
    </question>>>
  </hide-preamble>

  <doc-data|<doc-title|MAE5002 Homework3>|<doc-author|<author-data|<author-name|Zitong
  Huang>|<\author-affiliation>
    12432670@mail.sustech.edu.cn
  </author-affiliation>>>>

  <\question>
    \;

    <space|3em>(a) and (d). Since (a) is symmetric obviously, we will focus
    on (d)

    <space|3em>Proof of (d): Off-diagonal elemnts:

    <space|7em><math|a<rsub|i j>=2i-i j+2j>

    <space|7em><math|a<rsub|j i>=2j-i j+2i>

    <space|7em>Which is equavalent. So (d) is symmetric.
  </question>

  <\question>
    \;

    <space|3em>(a) Time of multiply: <math|M\<cdot\>N>

    <space|3em>(b) Time of addition: <math|M\<cdot\><around*|(|N-1|)>>
  </question>

  <\question>
    \;

    <space|3em>Division: <math|<below|<above|<big|sum>|N>|i=1>1=N>

    <space|3em>Multiply&Add&Sub: <math|<below|<above|<big|sum>|N>|i=1><around*|(|N-i|)>=<below|<above|<big|sum>|N-1>|k=1>k=<frac|<around*|(|N-1|)>N|2>=<frac|N<rsup|2>-N|2>>

    <space|3em>Thus, totally need <math|N> divisions,
    <math|<frac|N<rsup|2>-N|2>> multiplication and
    <math|<frac|N<rsup|2>-N|2>> addition / Subtraction
  </question>

  <\question>
    \;

    <space|3em>
  </question>
</body>

<\initial>
  <\collection>
    <associate|page-medium|paper>
  </collection>
</initial>