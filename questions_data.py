import random
# --- Data for Prepositions Quiz ---
PREPOSITIONS_DATA = {
    "Abhorrence of": ["Strong hatred or disgust for something"],
    "Abhorrent to": ["Causing disgust or hatred"],
    "Abide by": ["To follow or comply with a rule or decision"],
    "Abound with / Abound in": ["To be present in large numbers or amounts"],
    "Absolve from": ["To free from guilt, blame, or responsibility"],
    "Abstain from": ["To refrain from doing something"],
    "Abstemious in": ["Sparing or moderate in eating and drinking"],
    "Abstinence from": ["The practice of restraining oneself from indulging in something"],
    "Accede to": ["To agree to a demand, request, or treaty"],
    "Acceptable to": ["Satisfactory or allowed; Suitable"],
    "Access to": ["The means or opportunity to approach or enter a place"],
    "Accessible to": ["Able to be reached or entered"],
    "Accession to": ["The attainment of; The act of acceding to"],
    "Accompanied by": ["To go somewhere with someone"],
    "Accomplice of": ["A person who helps another commit a crime"],
    "Account for": ["To explain or justify"],
    "Accountable to": ["Responsible to someone for one's actions"],
    "Accused of": ["Charged with a wrongdoing or crime"],
    "Accustomed to": ["Familiar with something due to prolonged experience"],
    "Acquaint with": ["To make someone familiar with or aware of something"],
    "Acquaintance with": ["Knowledge or familiarity with something"],
    "Acquiesce in": ["To accept something reluctantly without protest"],
    "Acquit of": ["To free someone from a criminal charge"],
    "Act upon": ["To take action according to something, like information or advice"],
    "Adapt to": ["To adjust to new conditions"],
    "Addicted to": ["Unable to stop doing or using something"],
    "Adept at / Adept in": ["Very skilled or proficient at something"],
    "Adequate for": ["Sufficient for a particular purpose"],
    "Adhere to (rules)": ["To follow or stick to rules"],
    "Adjacent to": ["Next to or adjoining something"],
    "Admit into": ["To allow to enter a place or organization"],
    "Admit of": ["to allow something or make it possible"],
    "Admit to": ["To confess or acknowledge something"],
    "Advance by": ["To promote or move something forward"],
    "Advance for": ["To lend money for a particular purpose"],
    "Advise to": ["To recommend a course of action"],
    "Affable to": ["Friendly and easy to talk to"],
    "Affection for": ["A feeling of fondness or liking for someone or something"],
    "Affectionate to": ["Showing fondness or caring for"],
    "Affiliated to": ["Officially attached or connected to an organization"],
    "Affiliated with": ["Closely associated with a particular group or organization"],
    "Afflicted with": ["Suffering from something unpleasant, like a disease"],
    "Afraid of": ["Feeling fear or anxiety about something"],
    "Agree on": ["To come to a common understanding about something"],
    "Agree to": ["To give consent to"],
    "Agree with someone": ["To have the same opinion as someone else"],
    "Agreeable to": ["Willing to do something"],
    "Akin to": ["Similar to something"],
    "Alarmed at": ["Frightened or disturbed by something"],
    "Alien to": ["Unfamiliar, strange, or unrelated to something"],
    "Aim at": ["To target or intend to achieve something"],
    "Alight at": ["To step down onto something"],
    "Alight from": ["To step down from a vehicle"],
    "Alight on": ["To descend upon or find something"],
    "Alive to": ["Aware of or responsive to something"],
    "Allegiance to": ["Loyalty or commitment to a person or cause"],
    "Alliance with": ["A partnership or association with someone or something"],
    "Allowance for": ["To make accommodations or provisions for something"],
    "Aloof from": ["Distant or detached from a situation"],
    "Alternative to": ["Another option or possibility instead of something"],
    "Ambition for": ["A strong desire to achieve something"],
    "Amenable to": ["Open or responsive to an idea or suggestion"],
    "Amuse at / mock at / laugh at": ["Find something funny or entertaining"],
    "Amuse with": ["To entertain or occupy pleasantly"],
    "Analogous to": ["Similar or comparable to something"],
    "Angry at something / with someone": ["Anger towards something or someone"],
    "Annoy at": ["To be irritated by something"],
    "Annoy with": ["To irritate or bother someone"],
    "Answer by": ["To respond to something through a particular means"],
    "Answer to": ["To be accountable to someone"],
    "Answer for": ["To take responsibility for something"],
    "Answerable to": ["Responsible to someone or required to explain actions"],
    "Antidote against": ["Something that counteracts or prevents something undesirable"],
    "Antipathy against": ["A deep feeling of dislike towards someone or something"],
    "Antipathy to": ["A deep feeling of aversion towards something"],
    "Anxiety for": ["A feeling of worry or unease about something"],
    "Anxious about something": ["Feeling worried or concerned about something"],
    "Apologise to a person": ["To express regret to someone for an action"],
    "Apologize for": ["To express regret for an action or behavior"],
    "Appeal for": ["To make a serious or urgent request for something"],
    "Appetite for": ["A strong desire or liking for something"],
    "Applicable to": ["Relevant or appropriate to something"],
    "Apply for": ["To make a formal request for something, like a job"],
    "Apply to": ["To be relevant or applicable to something"],
    "Appoint to a post": ["To assign someone to a particular job or position"],
    "Apprehensive of": ["Anxious or fearful about something"],
    "Apprentice to": ["Someone who works for another to learn a trade"],
    "Apprise of": ["To inform someone of something"],
    "Approach to": ["A way of dealing with something"],
    "Appropriate to": ["Suitable or proper for something"],
    "Approve of": ["To give one's consent to"],
    "Aptitude for": ["A natural ability or skill at doing something"],
    "Argue with": ["To dispute or disagree with someone"],
    "Arrive at": ["To reach a place, decision, or conclusion"],
    "Arrive in": ["To reach a city, country, or other large area"],
    "Arrive on": ["To reach a specific day or date"],
    "Ashamed of": ["Embarrassed or guilty about something"],
    "Ask for": ["To request something"],
    "Aspirant of": ["Someone who has a strong desire to achieve something"],
    "Aspire to": ["To have a strong ambition to achieve something"],
    "Assent to": ["To agree to or approve of something"],
    "Assiduous in": ["Showing great care and perseverance in something"],
    "Associated with": ["Connected with something or someone else"],
    "Assurance of": ["A promise or guarantee of something"],
    "Assure of": ["To confidently tell someone something"],
    "Assured by": ["Given confidence by someone"],
    "Astonished at": ["Greatly surprised by something"],
    "Atone for": ["To make amends for something"],
    "Attachment to": ["A strong affection or connection to something"],
    "Attend to": ["To pay attention to something"],
    "Attend upon": ["To accompany or serve someone"],
    "Attending on": ["Accompanying or serving someone"],
    "Attention to": ["Focusing on or considering something"],
    "Attraction for": ["A liking or interest in something"],
    "Avail of": ["To make use of an opportunity or offer"],
    "Averse to": ["Having a strong dislike or opposition to something"],
    "Award for": ["To give something as a prize or honor for an achievement"],
    "Aware of": ["Having knowledge or realization of something"],
    "Bargain with": ["To negotiate with someone"],
    "Bathe in": ["To immerse oneself in a liquid"],
    "Bear with": ["To be patient or tolerant with someone or something"],
    "Bearing on": ["Relevance or influence on something"],
    "Beg of (a person)": ["To ask someone for something humbly"],
    "Beg pardon of": ["To apologize to someone"],
    "Begin on": ["To start something on a particular day"],
    "Begin with": ["To start from a particular point"],
    "Believe in": ["To have faith or confidence in something"],
    "Belong to": ["To be owned by someone or be a part of something"],
    "Beneficial to": ["Helpful or advantageous for something"],
    "Benefit by": ["To gain an advantage from something"],
    "Benefit from": ["To gain an advantage from something"],
    "Bent on": ["Determined to do something"],
    "Bereft of / Deprived of": ["Lacking or deprived of something"],
    "Beset with": ["Continuously troubled by something"],
    "Bestow (something) upon (a person)": ["To give something as an honor or gift"],
    "Beware of": ["To be cautious or wary of something"],
    "Bigoted on": ["Strongly prejudiced in favor of something"],
    "Blame for": ["To hold responsible for a fault or wrong"],
    "Blessed with": ["Endowed with something desirable"],
    "Blind to": ["Unaware or unperceptive of something obvious"],
    "Blind of": ["Unable to see due to a particular cause"],
    "Blush at": ["To feel embarrassed or ashamed about something"],
    "Blush for": ["To feel embarrassed or ashamed on behalf of someone"],
    "Boast of": ["To speak with excessive pride about something"],
    "Border on": ["To be close to an undesirable condition or quality"],
    "Borrow of or from a person": ["To take or receive something from someone with the intention of returning it"],
    "Bound for": ["Traveling towards a particular place"],
    "Bound with": ["Tied or secured with something"],
    "Break away": ["To escape or leave"],
    "Break down": ["To stop working or functioning properly"],
    "Break into": ["To enter forcibly"],
    "Break with": ["To end a relationship or association with someone"],
    "Bring down": ["To cause something to fall or collapse"],
    "Brush aside": ["To dismiss something as unimportant"],
    "Burdened with": ["Weighed down by something oppressive"],
    "Busy with": ["Actively engaged in doing something"],
    "But for": ["Without something or if something had not happened"],
    "Call at": ["To visit a place briefly"],
    "Call by": ["To pay a brief visit"],
    "Call off": ["To cancel something"],
    "Call on": ["To ask or demand that somebody do something"],
    "Callous to": ["Insensitive towards something"],
    "Candidate for": ["Someone who is being considered for a particular position or treatment"],
    "Capable of": ["Having the ability or qualities necessary to do something"],
    "Capacity for": ["The maximum amount that something can contain or produce"],
    "Careful about": ["Cautious or particular about something"],
    "Carry on": ["To continue doing something"],
    "Cash in on": ["To exploit or take advantage of something"],
    "Cater for": ["To provide what is needed or required"],
    "Cautious of": ["Wary or careful about something"],
    "Certain of": ["Completely sure about something"],
    "Characteristic of": ["A feature or quality belonging typically to a person, place, or thing"],
    "Charge against": ["A formal accusation of wrongdoing"],
    "Charge of": ["Responsibility or control of something"],
    "Charge with": ["To accuse someone formally of a crime"],
    "Claim on": ["A right to something"],
    "Clamour against": ["A loud and persistent demand, often in opposition to something"],
    "Clamour for": ["A loud and persistent demand for something, usually an action"],
    "Cling to": ["To hold onto something tightly"],
    "Close down": ["To cease business operations permanently"],
    "Close to": ["Near to something in distance or time"],
    "Come about": ["To happen or occur"],
    "Come from": ["To originate from a place"],
    "Come of": ["To be descended from or be the result of"],
    "Commence on / at / in / from": ["To begin or start something at a particular time or place"],
    "Commence with": ["To begin with a particular action or event"],
    "Commensurate with": ["Corresponding in size or degree to something else"],
    "Commit to": ["To pledge or bind to a certain course of action"],
    "Common to": ["Shared by two or more people or things"],
    "Comparable to": ["Similar or equivalent to something else"],
    "Compare to": ["To consider or describe as similar"],
    "Comparison with": ["An examination of two or more items to establish similarities and dissimilarities"],
    "Compassion for": ["Concern for the sufferings or misfortunes of others"],
    "Compatible with": ["Able to exist or perform in harmonious or agreeable combination"],
    "Compensate for": ["To make up for something"],
    "Competent for a job": ["Having the skills or ability to do a job"],
    "Complain about": ["To express dissatisfaction with or grumble about something"],
    "Complain against": ["To make a formal accusation or bring a charge against"],
    "Complain of": ["To state that one is suffering from something such as a pain or illness"],
    "Complain to": ["To express dissatisfaction or annoyance to someone about something"],
    "Compliment on": ["To express praise, commendation, or admiration to someone about something"],
    "Comply with": ["To act in accordance with a request, command, or instruction"],
    "Composed of": ["Made up of specified elements or parts"],
    "Compromise with": ["To arrive at an agreement by making concessions"],
    "Concede to": ["To yield or admit to something"],
    "Concern for": ["A feeling of worry or anxiety about something"],
    "Concerned with": ["Involved with or affected by something"],
    "Concession to": ["The act of allowing or yielding to something"],
    "Condemn to": ["Sentence someone to a particular punishment"],
    "Condole with": ["To express sympathy for someone in grief"],
    "Conducive to": ["Tending to promote or assist something"],
    "Confer honour on": ["To bestow an honor on someone"],
    "Confide in / to": ["To tell something to someone in confidence"],
    "Confidence in": ["A feeling of trust or belief in someone or something"],
    "Confident of": ["Having strong belief or full assurance about something"],
    "Conform to": ["To comply with rules, standards, or laws"],
    "Conformity with / to": ["Correspondence in form, manner, or character"],
    "Congenial to": ["Pleasant or agreeable because suited to one's taste or inclination"],
    "Congratulate on": ["To express congratulations to someone for something"],
    "Conscious of": ["Aware of something"],
    "Consent to": ["To give permission for or approval of something"],
    "Consist in": ["To have as an essential, necessary, or main element"],
    "Consist of": ["To be composed or made up of something"],
    "Consistent with": ["In agreement or harmony with something"],
    "Contempt for": ["A strong feeling of lack of respect for someone or something"],
    "Content with": ["In a state of peaceful happiness with something"],
    "Contrary to": ["Opposite in nature or character to something"],
    "Contrast to": ["Differ strikingly from something"],
    "Contrast with": ["To compare in such a way as to emphasize differences"],
    "Contribute to": ["To play a part in bringing something about"],
    "Control over": ["The power to make decisions about something"],
    "Conversant with": ["Familiar or acquainted with something"],
    "Convicted of": ["Having been found guilty of a criminal offense"],
    "Convinced of": ["Completely certain about something"],
    "Convulsed with": ["Affected by uncontrollable laughter or emotion"],
    "Cope with": ["To deal successfully with a difficult situation"],
    "Copy of": ["A reproduction or imitation of something"],
    "Cordon off": ["To prevent access to an area by surrounding it with police or other officials"],
    "Count on": ["To depend on someone or something"],
    "Courteous to": ["Polite and respectful to someone"],
    "Cover with": ["To place something over or on top of something else"],
    "Covetous of": ["Eagerly desirous of possessing something"],
    "Crave for": ["To have an intense desire for something"],
    "Criticism of": ["A negative assessment or remark about something"],
    "Cure for": ["Something that corrects a problem or relieves a disease"],
    "Cure of (a disease)": ["The successful treatment of a disease"],
    "Dabble in / at": ["To take part in an activity in a casual or superficial way"],
    "Deaf to": ["Unwilling or unable to listen or respond to something"],
    "Deal in": ["To do business that involves particular goods or services"],
    "Deal out": ["To distribute something"],
    "Deal with": ["To take appropriate action in a particular situation"],
    "Dear to": ["Regarded with deep affection by someone"],
    "Decamp with": ["To leave suddenly, taking something with you"],
    "Decide on / upon": ["To make a choice or reach a decision about something"],
    "Decline in": ["To become smaller, fewer, or less"],
    "Defective in": ["Having a fault or flaw"],
    "Deficient in": ["Not having enough of something"],
    "Delight at": ["To feel or express great pleasure in something"],
    "Delight in": ["To take great pleasure in something"],
    "Delighted with": ["Feeling or expressing great pleasure about something"],
    "Deliverance from": ["The act of being freed or saved from something unpleasant"],
    "Deluged with": ["To be overwhelmed by a large number of things"],
    "Deprive of": ["To prevent someone from having or doing something"],
    "Dependent on": ["Completely dependent on or influenced by something"],
    "Derogatory to": ["Tending to lessen the merit or reputation of something"],
    "Descent from": ["The origin or background of someone in terms of family or nationality"],
    "Desire for": ["A strong wish to have or do something"],
    "Desirous of": ["Having or characterized by desire"],
    "Desist from": ["To stop doing something"],
    "Despair of": ["To lose or give up hope"],
    "Destined for": ["Intended for or certain to have a particular fate"],
    "Destined to": ["Certain to do or have something"],
    "Destitute of": ["Completely lacking in something"],
    "Detach from": ["To separate or disconnect from something"],
    "Detrimental to": ["Tending to cause harm or damage to something"],
    "Devoid of": ["Entirely lacking or free from something"],
    "Devoted to": ["Feeling or displaying strong affection or dedication towards something"],
    "Die down": ["To become less strong or intense"],
    "Differ from": ["To be unlike or dissimilar to something"],
    "Differ on a point": ["To disagree about a specific point or subject"],
    "Differ with": ["To disagree with someone"],
    "Difference between": ["A point or way in which people or things are not the same"],
    "Different from": ["Unlike or dissimilar to something"],
    "Difficulty in": ["Problem or trouble in doing something"],
    "Diffident of": ["Lacking confidence in something"],
    "Diligent in": ["Showing persistent effort in doing something"],
    "Disappointed with": ["Feeling unhappy because someone or something was not as good as expected"],
    "Disastrous to": ["Extremely harmful or damaging"],
    "Discriminate against": ["To treat a person or group worse than others"],
    "Discriminate between": ["To recognize or perceive the difference between things"],
    "Discrimination in": ["The practice of treating one person or group differently from another in an unfair way"],
    "Disgrace on": ["The loss of respect, honor, or esteem"],
    "Disgrace to": ["A person or thing that brings shame or discredit"],
    "Disgust at / Disgust with": ["A strong feeling of dislike or disapproval caused by something unpleasant"],
    "Dispense with": ["To forgo or do without something"],
    "Displeased with": ["Feeling or showing irritation or dissatisfaction towards something"],
    "Dispose of": ["To get rid of or deal with something"],
    "Disposed to": ["Inclined or willing to do something"],
    "Dissolve in": ["To become absorbed in a liquid and form a solution"],
    "Distinguish between": ["To recognize or identify the difference between two things"],
    "Distinguish one thing from another": ["To recognize or identify the difference between two specific things"],
    "Divorce from": ["To legally end a marriage with someone"],
    "Doubt of": ["To have an uncertain opinion of something"],
    "Drag into": ["To involve someone in an unpleasant situation"],
    "Dream of": ["To imagine or fantasize about something"],
    "Drenched with": ["To be completely soaked or saturated with a liquid"],
    "Drive on": ["To continue traveling or making progress"],
    "Due to": ["Caused by or ascribable to something"],
    "Duty to": ["A moral or legal obligation towards someone"],
    "Dwell in": ["To live or reside in a place"],
    "Dwell on / upon": ["To think or speak about something at length"],
    "Eligible for": ["Qualified to participate in or receive something"],
    "Embark on": ["To begin a new project or venture"],
    "Enamoured of": ["Filled with love for or fascinated by something"],
    "Enamoured with (a person)": ["Filled with love for or fascinated by a person"],
    "Enchant with": ["To fill with delight or charm"],
    "End in": ["To have a particular result or outcome"],
    "Endowed with": ["Provided with a quality, ability, or asset"],
    "Engaged in": ["Busy or occupied with an activity"],
    "Engaged to": ["Committed to marry someone"],
    "Enlarge on / upon": ["To speak or write about something in more detail"],
    "Enmity to": ["A feeling of hostility or ill will towards someone or something"],
    "Enquire into (a matter)": ["To investigate or look into a matter"],
    "Enquire of (a person)": ["To ask someone for information"],
    "Enrage at": ["To make someone very angry about something"],
    "Enrage with": ["To fill someone with intense anger"],
    "Enter into": ["To become involved in or start to take part in something"],
    "Enter upon / on": ["To begin or start something"],
    "Entitled to": ["Having the right to do or have something"],
    "Enveloped in": ["Completely surrounded or covered by something"],
    "Envious of": ["Feeling or showing envy towards someone"],
    "Equal to": ["Having the same value, measure, or importance as something"],
    "Equivalent to": ["Equal in value, amount, meaning, or importance"],
    "Eradicate from": ["To completely remove or destroy something from a place"],
    "Escape from": ["To get away from a place, situation, or person"],
    "Essential for / to": ["Absolutely necessary for something"],
    "Exception to": ["Someone or something that does not follow a rule or pattern"],
    "Exchange for": ["To give or receive something in return for another thing"],
    "Exempt from": ["Not required to do something that others must do"],
    "Exemption from": ["The state of being released from an obligation or liability"],
    "Experience in": ["Knowledge or skill gained through being involved into something"],
    "Expert in": ["Having special knowledge or skill in a particular field"],
    "Exult at": ["To feel or show triumphant elation about something"],
    "Exult over": ["To rejoice or celebrate something"],
    "Failed in": ["Having been unsuccessful in achieving something"],
    "Failure of": ["The lack of success in doing or achieving something"],
    "Faithful to": ["Remaining loyal and steadfast to someone or something"],
    "Fall off": ["To become detached or to decline suddenly"],
    "Fall through": ["To fail to be completed or realized"],
    "False to": ["Not true to a standard or pattern"],
    "Familiar to": ["Well known or easily recognized by someone"],
    "Familiar with": ["Having good knowledge of or being well acquainted with something"],
    "Famous for": ["Known or recognized by many people for something"],
    "Far from": ["At a great distance in space or time from something"],
    "Fascinated by": ["Strongly attracted or interested in something"],
    "Fascinated with": ["Strongly attracted or interested in something"],
    "Fatal to": ["Causing death or disaster to someone or something"],
    "Fatigued with": ["Extremely tired from something"],
    "Fault with": ["A weakness or imperfection in someone or something"],
    "Favourable to": ["Expressing approval or support for someone or something"],
    "Fearful of": ["Feeling afraid or anxious about the possibility of something"],
    "Fed up with": ["Annoyed or unhappy because you have had too much of something"],
    "Feed on": ["To eat something as food regularly"],
    "Fell into": ["To suddenly enter an unpleasant situation or state"],
    "Felicitated on": ["To express or offer congratulations for something"],
    "Fight against": ["To try hard to stop or defeat something"],
    "Fill up": ["To make something completely full"],
    "Fill with": ["To put a large amount of something into a space"],
    "Fined for": ["To be required to pay an amount of money as a penalty"],
    "Fly into (anger)": ["To suddenly become very angry"],
    "Fond of": ["Having an affection or liking for someone or something"],
    "Fondness for": ["An affection or liking for someone or something"],
    "For lack of / For want of / For short of": ["Because there is not enough of something"],
    "Foreign to": ["Unfamiliar or strange to someone"],
    "Fortunate in / of": ["Having good luck or success in something"],
    "Free from (worries)": ["Not affected by or subject to something unpleasant"],
    "Free of cost": ["Without any payment required"],
    "Friendly with": ["Behaving in a pleasant, kind way towards someone"],
    "Full of": ["Containing a lot of something"],
    "Get at": ["Reach or understand"],
    "Get off": ["Leave a vehicle or remove clothing"],
    "Get on": ["Make progress or have a good relationship"],
    "Get out of": ["Avoid or leave"],
    "Get over": ["Recover from"],
    "Get rid of": ["Eliminate or discard"],
    "Gifted with": ["Endowed with"],
    "Give away": ["Reveal or distribute freely"],
    "Give out": ["Distribute or emit"],
    "Give up": ["Abandon or stop doing"],
    "Glance at": ["Look briefly at"],
    "Glance through": ["Read quickly"],
    "Go about": ["Begin or carry on with an activity"],
    "Go up": ["Increase"],
    "Good at": ["Skilled in"],
    "Good for": ["Beneficial"],
    "Grapple with": ["Struggle with"],
    "Grateful to": ["Thankful to"],
    "Greedy for / of": ["Having a strong desire for"],
    "Grieve at / for / over": ["Feel intense sorrow about"],
    "Grow up": ["Become an adult"],
    "Guard against": ["Take precautions against"],
    "Guard from": ["Protect from"],
    "Guess at": ["Estimate without certain knowledge"],
    "Guilty of": ["Responsible for wrongdoing"],
    "Hand over": ["Transfer or deliver"],
    "Hanker after": ["Have a strong desire for"],
    "Hard by": ["Close to"],
    "Hard up": ["Short of money"],
    "Hatred of or for something": ["Intense dislike for"],
    "Healed of": ["Cured of"],
    "Hear by": ["Learn from"],
    "Hear from": ["Receive communication from"],
    "Hear of": ["Be told about"],
    "Heartbroken on": ["Extremely sad about"],
    "Heedless of": ["Paying no attention to"],
    "Heir to": ["Inheritor of"],
    "Hide under": ["Conceal beneath"],
    "Hindrance to": ["Obstruction to"],
    "Hold up": ["Delay or support"],
    "Hinges on": ["Depends on"],
    "Honest in": ["Sincere in"],
    "Hope for": ["Wish for"],
    "Hopeful of": ["Optimistic about"],
    "Hostile to": ["Antagonistic toward"],
    "Hurtful to": ["Causing distress to"],
    "Ignorance of": ["Lack of knowledge about"],
    "Ignorant of": ["Lacking knowledge about"],
    "Ill with": ["Sick with"],
    "Immaterial to": ["Unimportant or irrelevant to"],
    "Impart to": ["Communicate knowledge to"],
    "Impertinent to": ["Irrelevant or inappropriate to"],
    "Impervious to": ["Unaffected by"],
    "Implicated in": ["Involved in wrongdoing"],
    "Impossible for": ["Not possible for"],
    "Impress upon": ["Emphasize to"],
    "Impress with": ["Make a good impression with"],
    "In Need of": ["Requiring"],
    "Incensed at": ["Extremely angry about"],
    "Inclined to": ["Tending toward"],
    "Increase in": ["Grow larger in number or amount"],
    "Indebted to": ["Owing gratitude to"],
    "Indifference / indifferent to": ["Lack of interest in"],
    "Indigenous to": ["Native to"],
    "Indignant at": ["Angry or resentful about"],
    "Indispensable to": ["Absolutely necessary"],
    "Indulge in": ["Enjoy or take part in"],
    "Infatuated with": ["Possessed with an intense but short-lived passion for"],
    "Infected with": ["Contaminated with"],
    "Infer from": ["Deduce from"],
    "Inference from": ["Conclusion drawn from"],
    "Inferior to": ["Lower in quality or rank"],
    "Infested with": ["Overrun or inhabited by (pests or undesirable things)"],
    "Influence on / over / with": ["Effect on"],
    "Informed of": ["Made aware of"],
    "Ingredients of": ["Components of"],
    "Inimical to": ["Harmful to"],
    "Injurious to": ["Harmful to"],
    "Innocent of": ["Not guilty of"],
    "Inquire after (welfare)": ["Ask about(someone's well-being)"],
    "Inquire for / about (a thing)": ["Ask for (information)"],
    "Inquire of": ["Ask (someone)"],
    "Inquired into": ["Investigated"],
    "Insensible to": ["Unaware of or unaffected by"],
    "Insight into": ["Deep understanding of"],
    "Insist on": ["Demand firmly"],
    "Inspired with": ["Filled with (a feeling)"],
    "Instill in": ["Gradually but firmly establish (an idea or attitude) in a person's mind"],
    "Interested in": ["Wanting to know or learn about"],
    "Interfere in": ["Intervene in"],
    "Interfere with": ["Prevent (a process or activity) from continuing or being carried out properly"],
    "Intimate with": ["Having a close and warm friendship with"],
    "Introduce to": ["Present (someone) to another person"],
    "Intrude into": ["Enter without invitation or permission"],
    "Intrude on": ["Interrupt or disturb"],
    "Inured to": ["Accustomed to"],
    "Invest with": ["To give authority or power to someone"],
    "Invite to": ["Ask (someone) to go somewhere or do something"],
    "Involved in": ["Taking part in"],
    "Irrelevant to": ["Not connected with or relevant to"],
    "Irrespective of": ["Without considering"],
    "Irritated against": ["Annoyed with"],
    "Irritated at": ["Annoyed by"],
    "Jealous of": ["Envious of"],
    "Jeer at": ["Mock or scoff at"],
    "Jest at": ["Joke about"],
    "Journey to": ["Travel to"],
    "Judge by": ["Form an opinion based on"],
    "Judge of": ["Form an opinion about"],
    "Judge to": ["Consider to be"],
    "Jump at": ["Accept eagerly"],
    "Juggling with": ["Manipulating"],
    "Jump into": ["Become suddenly involved in"],
    "Jump to": ["Come to (a conclusion) quickly"],
    "Junior to": ["Lower in rank or status"],
    "Keen on": ["Eager or excited about"],
    "Keep away from": ["Avoid"],
    "Keep on": ["Continue"],
    "Keep to": ["Adhere to"],
    "Keep up": ["Maintain"],
    "Key to": ["Solution or explanation of"],
    "Kind to": ["Behaving in a caring way towards"],
    "Knock against": ["Accidentally strike against"],
    "Knock at": ["Strike (a door) to attract attention"],
    "Knock on": ["Strike (a door) with the knuckles"],
    "Knock out": ["Make unconscious"],
    "Known by": ["Recognized by"],
    "Known for": ["Famous for"],
    "Known to": ["Familiar to"],
    "Laboured for": ["Worked hard for"],
    "Lack in": ["Be deficient in"],
    "Lack of": ["Shortage of"],
    "Laden with": ["Heavily loaded with"],
    "Lame in": ["Weak or ineffective in"],
    "Land at": ["Arrive at"],
    "Last for": ["Continue for"],
    "Late for": ["Arrive after the expected time for"],
    "Laugh at": ["Make fun of"],
    "Laugh over": ["Find amusement in"],
    "Laugh with": ["Share amusement with"],
    "Lax in": ["Not strict or severe in"],
    "Lead to": ["When one action or condition directly influences the outcome of another"],
    "Lead towards": ["Guide in the direction of"],
    "Lean against": ["Rest against for support"],
    "Lean on": ["Depend on"],
    "Lean to": ["Incline towards"],
    "Leave behind": ["Fail to take (someone or something)"],
    "Leisure for": ["Free time for"],
    "Leniency to": ["Mildness towards"],
    "Liable for": ["Legally responsible for"],
    "Liable to": ["Likely to experience"],
    "Lie between": ["Be situated between"],
    "Likeness between": ["Similarity between"],
    "Likeness to": ["Resemblance to"],
    "Liking for": ["Fondness for"],
    "Limit to": ["Restrict to"],
    "Listen to": ["Pay attention to"],
    "Live at": ["Reside at"],
    "Live by": ["To adhere to certain principles, rules, or guidelines in one's life"],
    "Live in": ["Reside in"],
    "Live off": ["Depend on for financial support"],
    "Live on": ["Survive on"],
    "Live within": ["Manage on (a limited budget)"],
    "Look after": ["Take care of"],
    "Look at": ["Direct one's gaze towards"],
    "Look down upon": ["Regard with contempt"],
    "Look for": ["Search or seek"],
    "Look into": ["Investigate"],
    "Look through": ["Examine or search through"],
    "Look up": ["Search for information"],
    "Lost to": ["Defeated by"],
    "Loyal to": ["Faithful to"],
    "Mad after/about/ on": ["Enthusiastic or obsessed"],
    "Mad with anger": ["Extremely angry"],
    "Made from": ["Produced using"],
    "Made of": ["Composed of"],
    "Malice against a person": ["III will towards someone"],
    "Married to": ["Wedded to"],
    "Marry off": ["Arrange a marriage for someone"],
    "Match for": ["Suitable partner fo"],
    "Meditate on (past act)": ["Reflect deeply on"],
    "Menace to": ["Threat to"],
    "Miss out": ["Fail to take advantage of"],
    "Mix with": ["Socialize with"],
    "Mock at": ["Ridicule"],
    "Most of": ["Majority of"],
    "Motive for / in": ["Reason for"],
    "Move by": ["Emotionally affected by"],
    "Move to": ["Relocate to"],
    "Move with": ["Accompany"],
    "Muse about / on / upon": ["Ponder or reflect on"],
    "Muse Over": ["Ponder or reflect on"],
    "Named after": ["Given the name of"],
    "Natural to": ["Inherent to"],
    "Necessary to": ["Essential for"],
    "Need for": ["Requirement of"],
    "Neglectful of": ["Failing to care for"],
    "Negligent / neglectful of": ["Careless about"],
    "Negligent in": ["Careless in"],
    "None but": ["No one except"],
    "Note for": ["A brief written message intended for a specific person"],
    "Obedience to": ["Compliance with"],
    "Obedient to": ["Compliant with"],
    "Object to": ["Oppose"],
    "Obliged to": ["Grateful to"],
    "Oblivious of": ["Unaware of"],
    "Obstruction to": ["Hindrance to"],
    "Occupied in": ["Engaged in"],
    "Occupied with / busy with": ["Engaged in"],
    "Occurred to": ["Came to mind"],
    "Offensive to": ["Displeasing to"],
    "Operate on / upon": ["Perform surgery on"],
    "Opportunity for": ["Chance for"],
    "Opposite to": ["Contrary to"],
    "Order for": ["Request for"],
    "Originate in": ["Begin in"],
    "Originate with": ["Begin with"],
    "Out of ": ["No longer in a stated place or condition"],
    "Overwhelm by / with": ["Overpower by"],
    "Owing to": ["Because of"],
    "Painful to": ["Causing pain to"],
    "Pardon of": ["Forgiveness for"],
    "Part from": ["Separate from"],
    "Part with": ["To give up possession or control of (something)"],
    "Partake of": ["join in (an activity) / consume in"],
    "Partial to": ["Favoritism"],
    "Partiality for": ["towards"],
    "Pass off": ["Pretend; evade"],
    "Pass through": ["Go through"],
    "Passion for": ["Strong liking for"],
    "Pay for": ["Cover the cost of"],
    "Peculiar to": ["Unique to"],
    "Penetrate into": ["Enter into"],
    "Perish by": ["Die by"],
    "Perish with": ["Die with"],
    "Persist in": ["Continue despite difficulties"],
    "Pertinent to": ["Relevant to"],
    "Pine away": ["To lose energy and become weak and feeble"],
    "Pine for": ["Long for"],
    "Pity for": ["Sympathy for"],
    "Play at": ["Engage in (a game or activity)"],
    "Play upon": ["Exploit or manipulate"],
    "Play with": ["Engage in (a game or activity)"],
    "Pleased with": ["Happy with"],
    "Pleasing to": ["Something that brings pleasure or happiness to someone"],
    "Pledged to": ["Committed to"],
    "Plot against": ["Conspire against"],
    "Ply between": ["Travel regularly between"],
    "Point at/out/to": ["Indicate"],
    "Poor at": ["Not good at"],
    "Popular for": ["Well-known for"],
    "Popular with": ["Well-liked by"],
    "Postscript to": ["Additional note to"],
    "Pour into": ["Flow into"],
    "Pray to": ["Worship"],
    "Precaution against": ["Safeguard against"],
    "Predilection for": ["Preference for"],
    "Preface to": ["Introduction to"],
    "Prefer to": ["Like better than"],
    "Preferable to": ["Better than"],
    "Prejudicial to": ["Detrimental to"],
    "Prepared for": ["Ready for"],
    "Present at": ["Attending"],
    "Present to / with": ["Give to"],
    "Preside at": ["to lead or be in charge of a meeting, ceremony, etc."],
    "Preside over": ["Supervise"],
    "Pretext for": ["Excuse for"],
    "Prevail against": ["Triumph over"],
    "Prevail on / upon": ["Persuade"],
    "Prevent from": ["Stop from"],
    "Prey on": ["Exploit or victimize"],
    "Pride in": ["Satisfaction with"],
    "Prior to": ["Before"],
    "Productive of": ["Causing"],
    "Proficient in": ["Skilled in"],
    "Profit by / from": ["Benefit from"],
    "Profitable to": ["Beneficial to"],
    "Prohibit from": ["Forbid from"],
    "Prompt in": ["Quick in"],
    "Prone to": ["Susceptible to"],
    "Proof of": ["Evidence of"],
    "Proud of": ["Pleased with"],
    "Provide with": ["Supply with"],
    "Provided against": ["Guarded against"],
    "Provided for": ["Supplied with"],
    "Pull over": ["Stop at the side of the road"],
    "Purchase of": ["Buying of"],
    "Put off": ["Postpone"],
    "Put out": ["Extinguish"],
    "Put up": ["Construct or erect something / display a notice, sign, or poster."],
    "Qualify for": ["Meet the requirements for"],
    "Quarrel over": ["Argue about"],
    "Quarrel with": ["Argue with"],
    "Quest for": ["Search for"],
    "Quick at / in": ["Fast at"],
    "Raise above": ["Elevate above"],
    "Ready for": ["Prepared for"],
    "Reason with": ["Persuade through logic"],
    "Rebel against": ["Resist or oppose"],
    "Reckon on / upon": ["Count on"],
    "Reconcile oneself to": ["Accept reluctantly"],
    "Reconcile to": ["Make compatible with"],
    "Reconcile with": ["Make peace with"],
    "Recourse to": ["Turning to for help"],
    "Recover from": ["Get better after"],
    "Reduced to": ["Decreased to"],
    "Reference to": ["Mention of"],
    "Refrain from": ["Abstain from"],
    "Regard for": ["Respect for"],
    "Regardless of": ["Despite"],
    "Rejoice at": ["Be happy about"],
    "Related to": ["Connected with"],
    "Relations with": ["Dealings with"],
    "Relevant to": ["Connected with"],
    "Rely on": ["Depend on"],
    "Remain in": ["Stay in"],
    "Remarkable for": ["Known for"],
    "Remind of": ["Cause to remember"],
    "Remiss in": ["Negligent in"],
    "Remonstrate with": ["Argue or protest"],
    "Remorse for": ["Regret for"],
    "Repent of": ["Feel regret for"],
    "Replace by": ["Substitute with"],
    "Replete with": ["Filled with"],
    "Reply to": ["Respond to"],
    "Repugnant to": ["Opposed to"],
    "Reputation for": ["Known for"],
    "Resemblance to": ["Similarity to"],
    "Resigned to": ["Accepting of"],
    "Resort to": ["Turn to"],
    "Respite from": ["Relief from"],
    "Rest with": ["Be decided by"],
    "Restored to": ["Returned to"],
    "Restricted to": ["Limited to"],
    "Result of": ["Outcome of"],
    "Retire from": ["Leave a job or position"],
    "Revenge on": ["Retaliate against"],
    "Revolt against": ["Rebel against"],
    "Rich in": ["Abundant in"],
    "Rival for": ["Competitor for"],
    "Rule over": ["Have authority over"],
    "Run into": ["Meet unexpectedly"],
    "Run on": ["Continue"],
    "Run over": ["Hit with a vehicle"],
    "Sacred to": ["Holy to"],
    "Sail on": ["Continue"],
    "Sanguine of": ["Optimistic about"],
    "Satiated with": ["Satisfied with"],
    "Satisfied with": ["Content with"],
    "Save from": ["Protect from"],
    "Search for": ["Look for"],
    "Search into": ["Investigate"],
    "Secret to": ["Unknown to"],
    "See into": ["Investigate"],
    "Seek after": ["Pursue"],
    "Seek for": ["Search for"],
    "Seeker of": ["One who looks for"],
    "Seething with": ["Filled with anger or excitement"],
    "Sensible of": ["Aware of"],
    "Sensitive to": ["Easily affected by"],
    "Sentence to": ["Condemn to"],
    "Sequel to": ["Continuation of"],
    "Set about": ["Begin"],
    "Set aside": ["Put to one side"],
    "Set in": ["Begin and seem likely to continue"],
    "Settle down": ["Become used to a new way of life"],
    "Shake with": ["Tremble with"],
    "Shocked at": ["Surprised and upset by"],
    "Short of": ["Lacking"],
    "Shout at": ["Yell at"],
    "Shout to": ["Yell to"],
    "Show off": ["Display ostentatiously"],
    "Sick of": ["Tired of"],
    "Side with": ["Support"],
    "Similar to": ["Resembling"],
    "Sit on": ["Be a member of (a committee, jury, or other body)"],
    "Slave to": ["Controlled by"],
    "Slip into": ["To put on clothes quickly / To go somewhere quietly or discreetly"],
    "Slow at": ["Not quick in"],
    "Smile at": ["Direct a smile at"],
    "Smile on": ["Favor"],
    "Soak in": ["Absorb"],
    "Solution to": ["Answer to"],
    "Sorry for": ["Feeling regret for"],
    "Spark off": ["Trigger"],
    "Speak for": ["Express support for"],
    "Speak of": ["Talk about"],
    "Spend beyond": ["Spend more than"],
    "Spring from": ["Originate from"],
    "Spring upon": ["Surprise or attack suddenly"],
    "Stand by": ["Support"],
    "Start for": ["Leave for"],
    "Start on": ["Begin a journey"],
    "Stay at": ["Reside temporarily at"],
    "Stay in": ["Remain indoors"],
    "Steeped in": ["Deeply involved in"],
    "Stick to": ["Adhere to"],
    "Stickler for": ["One who insists on"],
    "Strive for": ["Make great efforts to achieve"],
    "Strive with": ["Struggle with"],
    "Subject to": ["Dependent on"],
    "Submit to": ["Yield to"],
    "Subscription to": ["Regular payment to"],
    "Subsist on": ["Survive on"],
    "Substitute for": ["Replace with"],
    "Succeed in": ["Achieve success in"],
    "Succession to": ["Inheritance of"],
    "Succumb to": ["Die from"],
    "Suffer from": ["Be affected by (an illness)"],
    "Sufficient for": ["Enough for"],
    "Suggest to / Propose to": ["Recommend to"],
    "Suitable for": ["Appropriate for"],
    "Superior to": ["Better than"],
    "Supplement to": ["Addition to"],
    "Sure of": ["Certain of"],
    "Surprise at": ["Unexpected event"],
    "Surrender to": ["To give up control, power, or possession to someone or something, often after a struggle"],
    "Susceptible to": ["Easily affected by"],
    "Suspicious of": ["Distrustful of"],
    "Sympathetic to": ["Showing compassion for"],
    "Sympathise with": ["Feel or express sympathy for"],
    "Sympathy for": ["Compassion for"],
    "Take (Pity) on": ["Feel sorry for"],
    "Take care of": ["Look after"],
    "Take from": ["Steal from"],
    "Take Liking to": ["Develop fondness for"],
    "Take Pity on": ["Feel sorry for"],
    "Talk on": ["Discourse on"],
    "Talk over": ["Discuss"],
    "Talk to": ["Discuss with"],
    "Talk with": ["Converse with"],
    "Tantamount to": ["Equivalent to"],
    "Taste for": ["Liking for"],
    "Tear down": ["Demolish"],
    "Teeming with": ["Abundantly filled with"],
    "Temperate in": ["Moderate in"],
    "Temptation to": ["Desire to"],
    "Thank for": ["Express gratitude for"],
    "Think about": ["Consider"],
    "Think of": ["Imagine"],
    "Think over": ["Ponder"],
    "Think upon": ["Reflect on"],
    "Thirst for": ["Strong desire for"],
    "Thought of": ["Considered"],
    "Threaten with": ["Intimidate with"],
    "Throw at": ["Hurl at"],
    "Throw on": ["Cast light on"],
    "Tide over": ["Survive a difficult period"],
    "Tied up": ["Busy"],
    "Tired of": ["Weary of"],
    "Tolerant of": ["Accepting of"],
    "Touch with": ["Affect emotionally"],
    "Trade in": ["Buy and sell"],
    "Trade with": ["Do business with"],
    "Traitor to": ["Disloyal to"],
    "Travel over": ["Journey across"],
    "Treat of": ["Discuss"],
    "Tremble with": ["Shake with"],
    "Trespass against": ["Offend"],
    "Trespass on / upon": ["Encroach on"],
    "Trifle with": ["Treat casually"],
    "Triumph over": ["To win"],
    "True to": ["Faithful to"],
    "Trust in": ["Have confidence in"],
    "Turn down": ["Reject"],
    "Turn to": ["Seek help from"],
    "Turn up": ["To arrive, to appear"],
    "Under water": ["Beneath the surface of water"],
    "Upbraided for": ["Scolded for"],
    "Used to": ["Accustomed to"],
    "Useful for": ["Helpful for"],
    "Useful to": ["Beneficial to"],
    "Usher in": ["Mark the start of"],
    "Vain of": ["Excessively proud of"],
    "Venture upon": ["Undertake boldly"],
    "Versed in": ["Knowledgeable about"],
    "Vexed with / at": ["Annoyed by"],
    "Victory over": ["Triumph over"],
    "Violence on": ["Attack on"],
    "Void of": ["Lacking"],
    "Vote for": ["Choose in an election"],
    "Vote on": ["Decide by voting"],
    "Vote to": ["Make an official decision to"],
    "Wait for": ["Await"],
    "Wait until": ["Delay until"],
    "Wait upon": ["Serve"],
    "Waiting for": ["Anticipating"],
    "Want of": ["Lack of"],
    "Wanting in": ["Lacking in"],
    "Ward off": ["Protect from"],
    "Warn against": ["Caution against"],
    "Warn of": ["Inform about a potential danger"],
    "Warn off": ["Order to stay away"],
    "Way to": ["Means of"],
    "Weary of": ["Tired of"],
    "Wiped out": ["Eliminated"],
    "Wish for": ["Desire"],
    "With the exception of": ["Excluding"],
    "Withdraw from": ["Remove oneself from"],
    "Wonder at": ["Be amazed by"],
    "Work on": ["Engage in"],
    "Working on / Working in": ["Engaged in"],
    "Worried about": ["Anxious about"],
    "Worthy of": ["Deserving"],
    "Write on": ["Write about"],
    "Write to": ["Compose a letter to"],
    "Yearn for / Long for": ["Crave"],
    "Yield to": ["Surrender to"],
    "Zeal for": ["Enthusiastic devotion to"],
    "Zealous for / about": ["Passionate about"]
}

# --- Data for Phrasal Verbs Quiz (Sample) ---
# I've added a sample set. You can expand this with your own data.
PHRASAL_VERBS_DATA = {"Abide by": ["To follow a rule, decision, or instruction"],
    "Account for": ["To explain, give a reason"],
    "Act for": ["To represent"],
    "Act on": ["To take action because of something"],
    "Act out": ["To perform a narrative, To behave badly"],
    "Act up": ["Misbehave or malfunction"],
    "Add up": ["To make sense or calculate the total of"],
    "Advise against": ["To recommend not doing something"],
    "Agree with": ["To have the same opinion or accept a proposal"],
    "Aim at": ["To intend or direct at a target"],
    "Allow for": ["To take into consideration"],
    "Answer back": ["To reply rudely to someone in authority"],
    "Answer for": ["To take responsibility for something"],
    "Appeal to": ["To be attractive or interesting to"],
    "Apply for": ["To formally request something (like a job)"],
    "Ask after": ["To inquire about someone's health or well-being"],
    "Ask around": ["To ask many people the same question"],
    "Ask for": ["To request something"],
    "Ask out": ["To invite someone for a date"],
    "Attend on": ["To serve or provide assistance"],
    "Attend to": ["To deal with or pay attention to"],
    "Back away": ["To retreat or move backward"],
    "Back down": ["To withdraw a claim, demand, or commitment"],
    "Back off": ["To stop being involved; to withdraw"],
    "Back out": ["To withdraw from an agreement or commitment"],
    "Back up": ["To support; to make a copy of (for data)"],
    "Bail on": ["to leave someone"],
    "Bail out": ["To rescue from a difficult situation, especially financial"],
    "Bank on": ["To depend on something happening"],
    "Bank up": ["To accumulate or gather"],
    "Battle through": ["To struggle or fight through a difficult situation"],
    "Be in for": ["To be likely to experience something, usually unpleasant"],
    "Beam down": ["To transport or transmit down, often in sci-fi movies"],
    "Bear away": ["Carry someone or something away"],
    "Bear down": ["To apply strong pressure or force"],
    "Bear on/upon": ["To have an influence or effect on something"],
    "Bear out": ["To support or confirm"],
    "Bear up": ["To endure a difficult situation"],
    "Bear upon": ["To have relevance or influence on something"],
    "Bear with": ["To be patient with"],
    "Beat up": ["To physically attack"],
    "Become of": ["To happen to someone or something"],
    "Beef it up": ["To strengthen or make something more substantial"],
    "Beef something out": ["To add detail or information to something"],
    "Beef up": ["To strengthen or improve"],
    "Begin with": ["To start with something"],
    "Believe in": ["To have faith or confidence in something"],
    "Bet on": ["To have faith or confidence in; To gamble or speculate on something"],
    "Bite off": ["To separate or remove with teeth"],
    "Black out": ["To lose consciousness; to hide information"],
    "Block off": ["To separate using a barrier; to obstruct access"],
    "Blow away": ["To impress greatly; to remove or destroy something by an explosive force"],
    "Blow off": ["To ignore or fail to attend"],
    "Blow out": ["To extinguish; to rapidly deflate"],
    "Blow over": ["To pass without much effect"],
    "Blow up": ["To destroy by explosion; to enlarge"],
    "Boil down to": ["To reduce or simplify something to the most basic"],
    "Boot up": ["To start a computer"],
    "Bottle up": ["To suppress or hide emotions"],
    "Bow out": ["To withdraw or retire gracefully"],
    "Brace for": ["To prepare for something difficult or unpleasant"],
    "Branch out": ["To expand into new areas"],
    "Branch out into": ["To expand into a new area or field"],
    "Break away": ["To separate from a group"],
    "Break down": ["To stop working; to lose control of emotions"],
    "Break even": ["To have expenses equal income; no profit or loss"],
    "Break forth": ["To emerge suddenly"],
    "Break in": ["To interrupt or disturb something, to enter without consent or by force"],
    "Break off": ["To end abruptly"],
    "Break open": ["To force something to open"],
    "Break out": ["To start suddenly (war, disease, etc.)"],
    "Break out of": ["To escape from a place"],
    "Break through": ["To make an important discovery or advancement"],
    "Break up": ["To end a relationship; to separate into pieces"],
    "Break up with": ["To end a romantic relationship"],
    "Break with": ["To end a connection or tradition"],
    "Breeze through": ["To complete something easily and effortlessly"],
    "Brew up": ["To develop, often a plan or storm"],
    "Bring about/on": ["To cause something to happen"],
    "Bring along": ["To bring someone or something with oneself"],
    "Bring around": ["To convince; To restore to consciousness"],
    "Bring back": ["reintroduce something"],
    "Bring down": ["To reduce; to make unhappy"],
    "Bring forth": ["To produce or give birth to"],
    "Bring forward": ["To present; to reschedule for an earlier time"],
    "Bring in": ["To introduce; to generate (money)"],
    "Bring off": ["To successfully accomplish"],
    "Bring on": ["To cause to appear or occur"],
    "Bring out": ["To reveal or publish"],
    "Bring over": ["To personally transport or convince someone"],
    "Bring under": ["To subdue or get control of"],
    "Bring up": ["To raise a topic; to care for a child"],
    "Brush off": ["To ignore or disregard"],
    "Brush up": ["To improve or refresh one's knowledge"],
    "Bug out": ["To leave quickly, often due to fear or surprise"],
    "Build in": ["To include as an integral part"],
    "Build up": ["To increase or strengthen gradually"],
    "Bulk up": ["To gain muscle mass or size"],
    "Bump into": ["To meet unexpectedly"],
    "Bunk off": ["To skip or avoid, often school or work"],
    "Burn down": ["To destroy by fire completely"],
    "Burn out": ["To become exhausted; to stop functioning"],
    "Burn through": ["To use resources quickly or wastefully"],
    "Burn up": ["To destroy by fire; to make very angry"],
    "Burst out": ["To suddenly exclaim or express an emotion"],
    "Butt in": ["To interrupt or intrude rudely"],
    "Butt out": ["To stop interfering"],
    "Buy into": ["To completely believe in a concept or idea"],
    "Buzz off": ["To leave or exit"],
    "Call after": ["To name someone in honor of another"],
    "Call around": ["To phone several people for information or help"],
    "Call at": ["To visit or stop at (place) briefly"],
    "Call back": ["To return a phone call"],
    "Call by": ["To visit someone briefly"],
    "Call for": ["To require; to publicly ask for"],
    "Call forth": ["To evoke or draw out"],
    "Call in": ["To request to come; to inform by phone"],
    "Call in on": ["To visit someone, often for a short period"],
    "Call off": ["To cancel"],
    "Call on": ["To visit; to appeal to"],
    "Call out": ["To challenge; to identify publicly"],
    "Call up": ["To telephone someone"],
    "Call upon/on": ["To formally request someone to do something"],
    "Calm down": ["To become less agitated or upset"],
    "Camp out": ["To stay in a place temporarily, usually in a tent"],
    "Care for": ["To look after someone/something or to have affection for"],
    "Carry away": ["To become overly excited or to remove something"],
    "Carry off": ["To complete a task successfully or to win something"],
    "Carry on": ["To continue doing something"],
    "Carry out": ["To execute a plan or order"],
    "Carry through": ["To complete something difficult"],
    "Carve out": ["To establish a niche or role for oneself"],
    "Cash in": ["To profit from or to exchange"],
    "Cast away": ["To throw something away or to be stranded"],
    "Cast down": ["To feel depressed or saddened"],
    "Cast off": ["To discard or reject something"],
    "Catch on": ["To become popular or understood"],
    "Catch up": ["To reach someone who is ahead or to update on missed work"],
    "Cater to": ["To provide what is needed or desired"],
    "Chance upon": ["To find or encounter something by chance"],
    "Change into": ["To transform into something else"],
    "Change over": ["To switch from one thing to another"],
    "Charge with": ["To officially accuse someone of something"],
    "Cheat on": ["To be unfaithful to a partner"],
    "Cheat out of": ["To swindle or trick someone out of something"],
    "Check in": ["To register upon arrival at a hotel, airport, etc."],
    "Check in on": ["To visit or contact to ensure well-being"],
    "Check out": ["To leave a hotel; to investigate"],
    "Check through": ["To examine thoroughly or to process luggage to a final destination"],
    "Cheer on": ["To encourage or praise vocally"],
    "Cheer up": ["To become happier or to make someone feel happier"],
    "Chew out": ["To scold severely"],
    "Chew over": ["To think deeply about"],
    "Chicken out": ["To decide not to do something because of fear"],
    "Chip away at": ["To gradually reduce or drain away"],
    "Chip in": ["To contribute to something with others"],
    "Chop up": ["To cut something into pieces"],
    "Chuck out": ["To throw away or discard"],
    "Clam up": ["To become silent or refuse to speak"],
    "Clamp down on": ["To take strict action to prevent something"],
    "Clap back": ["To respond to criticism with a sharp retort"],
    "Clean out": ["To empty a space or area completely"],
    "Clean up": ["To tidy or clean a space"],
    "Clear of": ["To prove someone or something is not guilty or involved"],
    "Clear out": ["To remove items to make a space empty"],
    "Clear up": ["To make a place tidy or to resolve a misunderstanding"],
    "Clock in/out": ["To begin/end a work shift by recording the time"],
    "Clog up": ["To block or obstruct something"],
    "Close down": ["To cease operations or business"],
    "Close in": ["To surround or come closer"],
    "Close off": ["To close or block an opening; to separate something"],
    "Close up": ["To shut completely; to bring to a close"],
    "Coast through": ["To achieve something easily without much effort"],
    "Comb through": ["To search thoroughly"],
    "Come about": ["To happen or occur"],
    "Come across": ["To find or encounter by chance"],
    "Come along": ["To accompany someone or to make progress"],
    "Come apart": ["To separate into pieces or disintegrate"],
    "Come back": ["To return"],
    "Come by": ["To obtain or acquire something"],
    "Come clean": ["To be honest or confess"],
    "Come down": ["To decrease or descend"],
    "Come down to": ["To be essentially a matter of"],
    "Come down with": ["To become ill with"],
    "Come forward": ["To volunteer for something or to step ahead"],
    "Come from": ["To originate from"],
    "Come in": ["To enter or to be received"],
    "Come of": ["To result from"],
    "Come off": ["To take place; to happen or to succeed"],
    "Come on": ["To start, to happen; encouragement"],
    "Come out": ["To be published or become known"],
    "Come over": ["To visit casually"],
    "Come round": ["To change one's opinion or to regain consciousness"],
    "Come through": ["To survive a difficult situation or to receive something expected"],
    "Come through for": ["To provide needed support or assistance"],
    "Come to": ["To regain consciousness"],
    "Come up": ["To arise or occur"],
    "Come up with": ["To suggest or think of an idea or plan"],
    "Come upon": ["To find or discover by chance"],
    "Con into": ["To trick someone into doing something"],
    "Con out of": ["To deceive someone in order to take something from them"],
    "Cool off": ["To calm down or reduce in intensity"],
    "Cope with": ["To deal effectively with something difficult"],
    "Count on": ["To rely on or trust"],
    "Count up": ["To add together"],
    "Cover up": ["To conceal or hide something"],
    "Cozy up to": ["To become friendly or intimate with someone, often for personal gain"],
    "Crack down": ["To take severe action against something"],
    "Crack on": ["To continue or proceed quickly"],
    "Crash out": ["To fall asleep quickly or to be eliminated from a competition"],
    "Creep out": ["To cause someone to feel uneasy or scared"],
    "Crop up": ["To appear or occur suddenly or unexpectedly"],
    "Cross off": ["To remove from a list by drawing a line through"],
    "Crossout": ["To draw a line through something written"],
    "Curl up": ["To sit or lie in a position with legs close to the body"],
    "Cut across": ["To take a shorter route or affect different groups"],
    "Cut back": ["To reduce in amount or size"],
    "Cut down": ["To reduce consumption or to fell a tree"],
    "Cut in": ["To interrupt or insert"],
    "Cut it out": ["To stop doing something"],
    "Cut off": ["To sever or isolate"],
    "Cut out": ["To remove or stop doing something"],
    "Cut up": ["To cut into pieces or to be very upset"],
    "Date back": ["To originate or exist from a certain time"],
    "Dawn upon": ["To become clear or understood"],
    "Deal in": ["To trade in a specific type of goods"],
    "Deal with": ["To handle or confront a problem"],
    "Decide on": ["To make a choice about something"],
    "Delight in": ["To take great pleasure in"],
    "Depend on": ["To rely on"],
    "Deter from": ["To discourage from doing something"],
    "Devote to": ["To dedicate oneself or time to something"],
    "Die away": ["To diminish gradually"],
    "Die down": ["To decrease in intensity"],
    "Die for": ["To desire something greatly"],
    "Die out": ["To become extinct"],
    "Die-off": ["A significant reduction in population"],
    "Dig into": ["To investigate deeply or start eating"],
    "Dish out": ["To distribute or give away freely"],
    "Dispose of": ["To get rid of"],
    "Dive into": ["To start doing something with enthusiasm"],
    "Do away with": ["To abolish or eliminate"],
    "Do for": ["To ruin or kill someone or something"],
    "Do over": ["To redo or refurbish"],
    "Do up": ["To fasten or decorate"],
    "Do with": ["To benefit from having"],
    "Do without": ["To manage in the absence of something"],
    "Done for": ["In serious trouble or at the point of defeat or death"],
    "Done in": ["Extremely tired"],
    "Done with": ["To bring to an end; to finish"],
    "Dope out": ["To figure out or understand"],
    "Doze off": ["To fall asleep briefly, especially unintentionally"],
    "Draft in": ["To recruit or bring someone into a project or activity"],
    "Drag on": ["To continue for too long or tediously"],
    "Draw on": ["To use as a resource"],
    "Draw up": ["To come to a stop or to prepare a document"],
    "Dream of": ["To aspire or hope for"],
    "Dress up": ["To wear formal or elaborate clothes"],
    "Drift off": ["To gradually fall asleep"],
    "Drive away": ["To force to leave or flee"],
    "Drive out": ["To force someone or something to leave"],
    "Drive through": ["To use a service without leaving the car"],
    "Drop back": ["To move back in a group or position"],
    "Drop by": ["To visit casually or unexpectedly"],
    "Drop in": ["To visit informally"],
    "Drop off": ["To fall asleep or deliver something"],
    "Drop out": ["To withdraw from or quit"],
    "Drum up": ["To gather or obtain something"],
    "Dry off": ["To become dry"],
    "Dry out": ["To dehydrate or become sober"],
    "Dry up": ["To lose all moisture; to stop talking"],
    "Duck out": ["To leave secretly or abruptly"],
    "Dwell on": ["To think, speak, or write at length about something"],
    "Dwell upon": ["To think or contemplate deeply about something"],
    "Dying for": ["Desperately desiring something"],
    "Ease into": ["To gradually become familiar with or start doing something"],
    "Ease off": ["To reduce in severity or intensity"],
    "Eat into": ["To consume or deplete gradually"],
    "Eat out": ["To dine outside the home"],
    "Eat up": ["To consume completely"],
    "Edge out": ["To gradually defeat or surpass someone"],
    "Egg on": ["To encourage someone to do something, often something unwise"],
    "Embark on/upon": ["To start a new project or venture"],
    "Empty out": ["To remove the contents of something"],
    "End in": ["To result in a particular way"],
    "End up": ["To find oneself in a situation after a series of events"],
    "End with": ["To conclude with something specific"],
    "Engage in": ["To participate in an activity"],
    "Enter into": ["To begin or become involved in"],
    "Entitled to": ["To have the right to something"],
    "Entrust to": ["To give someone the responsibility for doing something"],
    "Entrust with": ["To give someone a thing to look after"],
    "Even up": ["To make equal or balanced"],
    "Expose to": ["To expose to, or cause to experience"],
    "Face down": ["To confront with determination or confront defiantly"],
    "Face up to": ["To confront or deal with a difficult situation"],
    "Fade away": ["To gradually disappear"],
    "Fall apart": ["To break into pieces; disintegrate"],
    "Fall back": ["To retreat or move back"],
    "Fall back on": ["To resort to something as an alternative"],
    "Fall behind": ["To lag or be delayed"],
    "Fall down": ["To collapse or fail"],
    "Fall flat": ["To fail to impress or amuse"],
    "Fall for": ["To be deceived or develop a romantic interest"],
    "Fall in": ["To get into position in a rank or formation"],
    "Fall in with": ["To agree with or become involved with"],
    "Fall off": ["To decrease in amount or intensity"],
    "Fall on": ["To attack or to be a responsibility of"],
    "Fall out": ["To quarrel or disagree; also, hair loss"],
    "Fall over": ["To lose one's balance and collapse"],
    "Fall through": ["To fail to happen or be completed"],
    "Fall to": ["To begin eagerly"],
    "Fan out": ["To spread out in a fan shape"],
    "Farm out": ["To delegate or send work to someone else"],
    "Feel for": ["To empathize or search by touching"],
    "Feel like": ["To have the desire or inclination"],
    "Feel up": ["To touch someone in a sexual way without consent"],
    "Feel up to": ["To feel capable or well enough to do"],
    "Ferret out": ["To discover or unearth information"],
    "Fight back": ["To defend oneself or retaliate"],
    "Fight off": ["To repel or resist"],
    "Figure on": ["To plan or expect"],
    "Figure out": ["To understand or solve"],
    "Fill in": ["To complete (an area or information)"],
    "Fill out": ["To complete (a form, details)"],
    "Fill up": ["To make full"],
    "Find out": ["To discover"],
    "Finish off": ["To complete or end something"],
    "Fire away": ["To begin to speak or ask questions freely; To fire a gun repeatedly"],
    "Fire up": ["To ignite or set alight; To activate"],
    "Firm up": ["To make firm or more definite"],
    "Fish for": ["To seek or probe for information"],
    "Fish out": ["To retrieve something from within"],
    "Fit in": ["To be compatible or get along"],
    "Fix up": ["To repair or arrange"],
    "Fizzle out": ["To end weakly or ineffectively"],
    "Flake out": ["To fail to meet an obligation or to fall asleep"],
    "Flare up": ["To suddenly become angry or intense"],
    "Flat line": ["To die or cease living; To fail to make any progress"],
    "Flick through": ["To quickly browse or skim through, especially reading material"],
    "Flip out": ["To react extremely or lose control"],
    "Flirt with": ["To show attraction or interest in a light-hearted manner"],
    "Float around": ["To circulate, especially of rumors or ideas"],
    "Flood in": ["To arrive in large numbers or quantities"],
    "Fly open": ["To open suddenly or forcefully"],
    "Focus on": ["To concentrate on"],
    "Follow up": ["To continue or further investigate"],
    "Fool around": ["To behave in a silly or non-serious manner"],
    "Force into": ["To compel to enter or engage"],
    "Fork out": ["To pay, especially reluctantly"],
    "Freak out": ["To react with extreme emotion, panic, or agitation"],
    "Free up": ["To make available by removing restrictions or obstructions"],
    "Freeze over": ["To become covered with ice"],
    "Freshen up": ["To refresh oneself, e.g., by washing or changing clothes"],
    "Fritter away": ["To waste time, money, or energy on trivial activities"],
    "Frown upon": ["To disapprove of something"],
    "Gain on": ["To get closer to someone or something in a chase or competition"],
    "Gather around": ["To come together around someone or something"],
    "Gear up": ["To prepare for an event or activity"],
    "Get across": ["To communicate an idea or message effectively"],
    "Get ahead": ["To advance or succeed"],
    "Get along": ["To have a good relationship"],
    "Get around": ["To circulate; also, to find a way to overcome a problem"],
    "Get around to": ["To finally find time to do something"],
    "Get at": ["To imply something; To acquire or gain possession of (something)"],
    "Get away": ["To escape"],
    "Get away with": ["To do something wrong without being caught or punished"],
    "Get back": ["To return"],
    "Get back at": ["To retaliate or take revenge"],
    "Get back into": ["To become involved in something again"],
    "Get back to": ["To return to a place, topic, or activity"],
    "Get behind": ["To support; also, to fall behind schedule"],
    "Get by": ["To manage to survive or cope"],
    "Get by with": ["To manage to survive or do moderately well with limited resources"],
    "Get down": ["To descend; to focus on something; to feel depressed"],
    "Get down to": ["To start to seriously focus on or deal with something"],
    "Get in": ["To enter a place or vehicle"],
    "Get into": ["To become involved in a situation or activity"],
    "Get off": ["To leave a vehicle; To stop doing something"],
    "Get off on": ["To enjoy something, often in a sexual sense"],
    "Get on": ["To enter or board (a vehicle); to progress"],
    "Get on with": ["To continue doing something; to have a good relationship"],
    "Get out": ["To leave a place; To circulate or spread"],
    "Get out of": ["To avoid doing something"],
    "Get over": ["To recover from an ailment or an emotional setback"],
    "Get over with": ["To finish something that is difficult or unpleasant"],
    "Get rid of": ["To eliminate or discard"],
    "Get round": ["To persuade someone to agree; to circumvent"],
    "Get the sack": ["To be dismissed from employment"],
    "Get through": ["To successfully make contact; to complete"],
    "Get to": ["To arrive; To succeed in influencing"],
    "Get together": ["To meet and spend time together"],
    "Get up": ["To rise from bed; to stand up"],
    "Give away": ["To reveal a secret or to give something as a gift"],
    "Give back": ["To return something to its original owner"],
    "Give in": ["To surrender or submit"],
    "Give off": ["To emit a smell, light, heat, etc."],
    "Give out": ["To distribute or to become exhausted"],
    "Give over": ["To stop doing something; to hand over"],
    "Give up": ["To quit or surrender"],
    "Give way": ["To collapse or yield"],
    "Given to": ["Prone to or inclined to do something"],
    "Gloss over": ["To cover up or treat superficially without going into depth"],
    "Gnaw away at": ["To destroy in a gradual manner; To cause persistent distress or anxiety"],
    "Go about": ["To proceed with a task or to circulate"],
    "Go after": ["To pursue or chase"],
    "Go against": ["To oppose or be contrary to"],
    "Go ahead": ["To proceed or continue"],
    "Go along with": ["To agree or cooperate with"],
    "Go around": ["To circulate, To bypass or avoid, to visit various places"],
    "Go at": ["To attack or approach aggressively"],
    "Go away": ["To leave or depart"],
    "Go back": ["To return to a place or condition"],
    "Go back on": ["To break a promise or fail to fulfill"],
    "Go bananas": ["To become very angry or excited"],
    "Go beyond": ["To exceed or surpass"],
    "Go blank": ["To be unable to remember or think of something"],
    "Go bust": ["To become bankrupt"],
    "Go by": ["To pass (time) or to adhere to"],
    "Go down": ["To decrease, happen, or be received"],
    "Go downhill": ["To deteriorate in quality or condition"],
    "Go for": ["To choose or attempt"],
    "Go in for": ["To have an interest or participate in"],
    "Go in/into": ["To enter"],
    "Go off": ["To explode or begin"],
    "Go on": ["To continue or happen"],
    "Go out": ["To leave, especially for social activities"],
    "Go over": ["To review or examine"],
    "Go overboard": ["To do something excessively"],
    "Go through": ["To experience or live through something"],
    "Go together": ["To match or be suitable together"],
    "Go up": ["To increase in price, amount, or level"],
    "Go with": ["To match or accompany"],
    "Go without": ["To endure the absence of something"],
    "Goof around": ["To waste time doing nothing serious"],
    "Goof up": ["To make a mistake"],
    "Grapple with": ["To struggle with a problem"],
    "Grin at": ["To smile broadly at"],
    "Gross out": ["To disgust someone deeply"],
    "Grow apart": ["To become less close over time"],
    "Grow back": ["To regrow after being cut or lost"],
    "Grow into": ["To mature or develop into"],
    "Grow out of": ["To develop from; also to outgrow something"],
    "Grow up": ["To mature or become an adult"],
    "Hammer out": ["To negotiate and agree on something"],
    "Hand back": ["To return something to its original holder"],
    "Hand down": ["To give something to a younger generation"],
    "Hand in": ["To submit something officially"],
    "Hand on": ["To pass something to the next person or generation"],
    "Hand out": ["To distribute something to a group of people"],
    "Hand over": ["To give control or possession of something"],
    "Hang about": ["To spend time in a place aimlessly"],
    "Hang around": ["To stay in the same place, postion or level"],
    "Hang in": ["To persevere or remain persistent"],
    "Hang of something": ["To understand or get used to something"],
    "Hang on": ["To hold tightly; to wait a short time"],
    "Hang onto": ["To keep something; not give away or lose"],
    "Hang out": ["To spend time relaxingly in a place or with someone"],
    "Hang together": ["To remain united or coherent"],
    "Hang up": ["To end a phone call; to suspend something"],
    "Harpon": ["To talk about something repeatedly in an annoying way"],
    "Hash out": ["To discuss thoroughly and reach an agreement"],
    "Have against": ["To hold a grudge or have a reason for dislike"],
    "Have on": ["To be wearing something; to deceive"],
    "Have words with": ["To have a serious conversation, often involving reprimand"],
    "Head back": ["To return to a place"],
    "Head for": ["To go in the direction of"],
    "Head off": ["To prevent something from happening"],
    "Head out": ["To depart or leave a place"],
    "Head toward": ["To move in the direction of something"],
    "Hear about": ["To be informed of something"],
    "Hear from": ["To receive news or communication from someone"],
    "Hear of": ["To know about the existence of something"],
    "Heat up": ["To make or become hot"],
    "Help out": ["To assist someone"],
    "Hide away": ["To conceal oneself or something in a secure place"],
    "Hit back": ["To retaliate or respond to an attack"],
    "Hit on": ["To suddenly think of an idea"],
    "Hive off": ["To separate part of a company or organization"],
    "Hold against": ["To have a grudge or negative feeling towards someone"],
    "Hold back": ["To restrain or withhold something or someone"],
    "Hold down": ["To keep something at a low level; to maintain a job"],
    "Hold off": ["To delay doing something; also to keep someone at a distance"],
    "Hold on": ["To wait or pause; also, to grasp tightly"],
    "Hold onto": ["To keep possession of; to cling to"],
    "Hold out": ["To resist or endure"],
    "Hold out for": ["To wait for a specific outcome or condition"],
    "Hold over": ["To extend the duration of; to postpone"],
    "Hold up": ["To delay or rob; also to support"],
    "Hold with": ["To agree with or endorse"],
    "Home in on": ["To focus closely on a target or objective"],
    "Hook up": ["To connect or attach something; also, to form a relationship"],
    "Hunt down": ["To search for and capture"],
    "Hurry up": ["To increase speed or quicken the pace"],
    "Hush up": ["To keep something secret or to quieten"],
    "Identify with": ["To feel a strong connection or similarity with"],
    "Impact on": ["To have a significant effect on something"],
    "Impose on": ["To unfairly place demands on someone"],
    "Impress on": ["To strongly convey the importance of something to someone"],
    "Improve on/upon": ["To make or become better than before"],
    "Infer from": ["To deduce or conclude information from evidence"],
    "Ink in": ["To schedule or confirm in a definite manner"],
    "Insist on": ["To demand something forcefully, without accepting refusal"],
    "Interfere with": ["To prevent or slow down a process or activity"],
    "Invest in": ["To put money, effort, time, etc., into something to achieve a profit or result"],
    "Involve in": ["To include someone or something in an activity"],
    "Iron out": ["To remove difficulties or find solutions to problems"],
    "Jack up": ["To increase, usually prices or physically lift something"],
    "Jam into": ["To force into a small or insufficient space"],
    "Jam up": ["To become or make something blocked or stuck"],
    "Jockey for position": ["To maneuver or compete for a better position"],
    "Join in": ["To participate in an activity with others"],
    "Join up": ["To enlist in the military; to connect"],
    "Jot down": ["To write something quickly"],
    "Juice up": ["To make something more lively or exciting"],
    "Jumble up": ["To mix things together in a disorganized way"],
    "Jump at": ["To quickly accept a chance or opportunity"],
    "Jump in": ["To enter suddenly or join in spontaneously"],
    "Jump on": ["To criticize or attack someone quickly"],
    "Jump to": ["To arrive at a conclusion hastily"],
    "Keel over": ["To fall down or faint"],
    "Keep at": ["To continue doing something, especially work"],
    "Keep away": ["To avoid getting near"],
    "Keep back": ["To stay at a distance; to withhold information"],
    "Keep down": ["To control or suppress"],
    "Keep from": ["To prevent someone from doing something"],
    "Keep in with": ["To maintain good relations with someone"],
    "Keep off": ["To not go onto or touch something"],
    "Keep on": ["To continue doing something"],
    "Keep out": ["To prevent from entering"],
    "Keep out of": ["To stay away from or not get involved"],
    "Keep to": ["To stick to a path, decision, or rule"],
    "Keep up": ["To maintain a certain level"],
    "Keep up with": ["To stay at the same level as someone or something"],
    "Kick against": ["To resist or oppose"],
    "Kick around": ["To discuss casually; to mistreat or abuse"],
    "Kick back": ["To relax; to pay someone illicitly as a bribe"],
    "Kick off": ["To start or initiate; also the start of a football game"],
    "Kick out": ["To force someone to leave"],
    "Kill off": ["To completely eliminate or destroy"],
    "Knock about/around": ["To travel without a clear purpose; to be treated badly"],
    "Knock down": ["To demolish or reduce in price"],
    "Knock off": ["To stop working; to produce something cheaply"],
    "Knock out": ["To defeat and remove from competition; to render unconscious"],
    "Knock over": ["To accidentally hit and cause to fall"],
    "Know about": ["To be informed about something"],
    "Know of": ["To be aware of something or someone"],
    "Laid up with": ["To be confined to bed due to illness"],
    "Lash into": ["To attack or criticize severely"],
    "Lash out": ["To suddenly attack verbally or physically"],
    "Latch on to": ["To understand or adopt an idea quickly"],
    "Laugh at": ["To make fun of someone or something"],
    "Laugh off": ["To dismiss something by laughing"],
    "Launch into": ["To start something with enthusiasm"],
    "Lay aside/by": ["To save or put away (Money) for future use"],
    "Lay down": ["To establish rules or principles; to lie down"],
    "Lay in": ["To acquire and store a supply of something"],
    "Lay off": ["To temporarily or permanently dismiss from employment"],
    "Lay out": ["To arrange or design; also, to spend money"],
    "Layer up": ["To wear multiple layers of clothing"],
    "Laze around": ["To relax and do very little"],
    "Lead to": ["To result in or cause"],
    "Lead up to": ["To precede a particular event or time"],
    "Leak out": ["To become known accidentally or unofficially"],
    "Learn about": ["To acquire knowledge or information about something"],
    "Leave behind": ["To forget to take something; to outperform others"],
    "Leave off": ["To stop doing something"],
    "Leave out": ["To exclude"],
    "Leave over": ["To cause to remain unconsumed or undone till a future time"],
    "Leave to": ["To allow someone to make a decision or take responsibility"],
    "Leave/Let alone": ["To not disturb or bother"],
    "Let down": ["To disappoint"],
    "Let fly": ["To suddenly express anger or to release something quickly"],
    "Let in": ["To allow someone to enter"],
    "Let in on": ["To share a secret or confidential information"],
    "Let into": ["To allow entry into a group or place"],
    "Let off": ["To release someone from punishment; to emit"],
    "Let on": ["To reveal or disclose information"],
    "Let out": ["To allow someone or something to leave a place"],
    "Let up": ["To decrease in intensity"],
    "Lick into shape": ["To organize or improve something to reach an acceptable standard"],
    "Lie around": ["To be left untidily around a place; to be lazy"],
    "Lie behind": ["To be the cause or reason for something"],
    "Lie in": ["To stay in bed later than usual"],
    "Lift up": ["To raise something or someone"],
    "Light on": ["To discover or encounter"],
    "Light up": ["To illuminate; to become happy or excited"],
    "Lighten up": ["To become more relaxed or easier to deal with"],
    "Limber up": ["To warm up and stretch the muscles before exercise"],
    "Line up": ["To arrange in a line; to organize"],
    "Live by": ["To adhere to particular principles"],
    "Live for": ["To exist for a particular purpose"],
    "Live off": ["To rely on someone for a source of income or support"],
    "Live on": ["To continue to exist; to subsist on"],
    "Live through": ["To survive a difficult situation, period or event"],
    "Live up to": ["To meet or fulfill expectations"],
    "Live with": ["To accept and deal with a difficult situation"],
    "Load up": ["To fill with a large amount"],
    "Lock down": ["To secure or confine"],
    "Lock in": ["To put(someone or something) in a locked place"],
    "Lock out": ["To prevent from entering by locking the door"],
    "Lock up": ["To secure or imprison"],
    "Log in (or on)": ["To enter a computer system by typing a username and password"],
    "Log out (or off)": ["To exit a computer system"],
    "Long for": ["To desire something greatly"],
    "Look about": ["To try to locate someone or something"],
    "Look after": ["To take care of"],
    "Look around": ["To explore or search a place by looking"],
    "Look at": ["To consider or examine"],
    "Look back on": ["To remember and reflect on the past"],
    "Look down on": ["To consider someone or something as inferior"],
    "Look for": ["To search for"],
    "Look forward to": ["To anticipate with pleasure"],
    "Look in on": ["To visit briefly"],
    "Look into": ["To investigate or examine"],
    "Look on": ["To watch without getting involved"],
    "Look on as": ["To consider or regard in a specific way"],
    "Look out": ["To be cautious or wary"],
    "Look out for": ["To take care of somebody and make sure nothing bad happens to them"],
    "Look over": ["To examine or review"],
    "Look to": ["To depend on or expect something from someone"],
    "Look up": ["To search for information"],
    "Look up to": ["To admire or respect someone"],
    "Look upon": ["To consider or view in a certain way"],
    "Luck into": ["To achieve something by chance"],
    "Luck out": ["To have an unexpected good fortune"],
    "Make do": ["To manage with the available resources"],
    "Make for": ["To go in a certain direction; to contribute to"],
    "Make fun of": ["To mock or ridicule"],
    "Make into": ["To transform something into something else"],
    "Make of": ["To understand or interpret"],
    "Make off": ["To escape of flee"],
    "Make off with": ["To steal something and escape with something"],
    "Make off with/away with": ["To steal something and escape with it"],
    "Make out": ["To discern or understand; to manage"],
    "Make over": ["To transfer ownership; to transform"],
    "Make the most of": ["To take full advantage of something"],
    "Make up": ["To reconcile; to invent; to apply cosmetics"],
    "Make up for": ["To compensate for a deficiency or mistake"],
    "Map out": ["To plan or outline in detail"],
    "Mark off": ["To delineate or separate by marking"],
    "Match up": ["To compare or be equivalent"],
    "Max out": ["To reach a maximum limit"],
    "Measure up": ["To meet expectations or standards; to be good enough"],
    "Measure up to": ["To be as good as something"],
    "Meet with": ["To encounter, often by accident; to have a meeting"],
    "Mess about": ["To spend time idly or without purpose"],
    "Mess around": ["To waste time; to engage in idle activities"],
    "Mess up": ["To make a mistake or mishandle something"],
    "Mess with": ["To interfere or meddle inappropriately"],
    "Miss out": ["To lose the chance or opportunity"],
    "Mist up": ["To become covered with mist"],
    "Mistake for": ["To incorrectly identify someone or something"],
    "Mix up": ["To confuse or combine in a disorderly way"],
    "Monkey around with": ["To tamper or play with in an irresponsible way"],
    "Mop up": ["To clean or absorb something completely"],
    "Mope around": ["To move around in a listless or aimless manner"],
    "Mount up": ["To increase over time"],
    "Mouth off": ["To speak loudly and aggressively without respect"],
    "Move in": ["To start living in a new residence"],
    "Move on": ["To proceed or advance in action"],
    "Move out": ["To leave a residence or location"],
    "Move up": ["To advance to a higher position or place"],
    "Muddle through": ["To manage to do something despite difficulties"],
    "Mow down": ["To cut down grass; to kill or knock down"],
    "Mull over": ["To think carefully about something"],
    "Muscle in on": ["To force one's way into a situation uninvited"],
    "Nag at": ["To continually complain or criticize"],
    "Nail down": ["To finalize or secure something"],
    "Nail it": ["To perform a task exceptionally well"],
    "Name after": ["To give someone or something the same name as another"],
    "Name-drop": ["To mention famous people one knows to impress others"],
    "Narrow down": ["To reduce the number of possibilities"],
    "Nod off": ["To fall asleep unintentionally"],
    "Nose out": ["To discover or find out by investigation"],
    "Note down": ["To write something down for future reference"],
    "Nurse back to health": ["To care for someone until they recover health"],
    "Nut out": ["To solve a difficult problem"],
    "Object to": ["To express disagreement or opposition"],
    "Occur to": ["To come into one's mind"],
    "Open out": ["To unfold or become more accessible"],
    "Open up": ["To make available or reveal"],
    "Opt for": ["To choose or decide on"],
    "Opt in": ["To choose to participate"],
    "Opt out of": ["To choose not to participate"],
    "Opt-out": ["To withdraw or exclude oneself from an arrangement"],
    "Order about/around": ["To command or direct people in a domineering way"],
    "Order off": ["To demand someone to leave"],
    "Overcome": ["To successfully deal with or gain control over something"],
    "Overcome with": ["To be overwhelmed by an emotion or reaction"],
    "Overlook": ["To fail to notice or deliberately ignore"],
    "Owe to": ["To be under obligation to pay or repay in return for something received"],
    "Own up": ["To admit or confess something"],
    "Pack away": ["To put something in its proper place, especially for storage"],
    "Pack in": ["To stop or quit"],
    "Pack into": ["To fill a space with people or things"],
    "Pack up": ["To put things into boxes or bags at the end of an activity"],
    "Pad out": ["To add unnecessary content to extend something"],
    "Paper over": ["To hide problems or difficulties"],
    "Part from": ["To leave or separate from"],
    "Part with": ["To give up possession of something"],
    "Pass around": ["To distribute or circulate among a group"],
    "Pass away": ["To die"],
    "Pass by": ["To go past; to let an opportunity go without taking action"],
    "Pass for": ["To be accepted as or believed to be something"],
    "Pass into": ["To enter a particular state or condition"],
    "Pass off": ["To happen, especially without complications"],
    "Pass off as": ["To pretend that something is a particular thing when it is not"],
    "Pass on": ["To give something to another person"],
    "Pass oneself off": ["To pretend to be someone else"],
    "Pass out": ["To lose consciousness"],
    "Pass over": ["To ignore or overlook"],
    "Pass through": ["To go from one side to the other; to experience"],
    "Pass up": ["To decline or refuse an opportunity"],
    "Pat down": ["To search someone by tapping their clothing"],
    "Patch up": ["To repair or mend a relationship or item"],
    "Pay back": ["To return money that is owed; to revenge"],
    "Pay for": ["To give money in exchange for goods or services"],
    "Pay off": ["To result in success; to finish paying a debt"],
    "Pay up": ["To settle a debt by paying"],
    "Peel off": ["To remove the outer layer"],
    "Perk up": ["To become or make more lively"],
    "Phase out": ["To gradually stop using something"],
    "Pick on": ["To bully or criticize persistently"],
    "Pick out": ["To select or choose"],
    "Pick up": ["To lift; to improve; to collect someone or something"],
    "Pig out": ["To eat excessively"],
    "Pile up": ["To accumulate or stack up"],
    "Piss off": ["To annoy or anger"],
    "Plan for": ["To make preparations for a specific situation"],
    "Plan on": ["To intend to do something"],
    "Play around": ["To behave in a frivolous manner"],
    "Play at": ["To pretend to be: to engage in an activity superficially"],
    "Play back": ["To reproduce recorded material"],
    "Play down": ["To minimize the importance"],
    "Play on/upon": ["To exploit a characteristic or sentiment"],
    "Plough through": ["To work through something difficult"],
    "Plug in": ["To connect an electrical device to a power source"],
    "Plug up": ["To block or fill a hole or gap"],
    "Plump for": ["To choose decisively"],
    "Plunk down": ["To put down heavily or carelessly"],
    "Point out/to": ["To draw attention to something or someone by pointing"],
    "Polish off": ["To finish or consume completely"],
    "Pony up": ["To pay or contribute money"],
    "Pore over": ["To study or read something carefully"],
    "Pot up": ["To transfer a plant into a pot"],
    "Pour in": ["To arrive or enter in large numbers"],
    "Power through": ["To continue with strength despite difficulties"],
    "Print out": ["To produce a hard copy of a document from a computer"],
    "Prize out": ["To remove with effort or difficulty"],
    "Psych out": ["To intimidate or ourwit psychologically"],
    "Pull apart": ["To separate forcefully; to criticize severely"],
    "Pull back": ["To withdraw or retreat"],
    "Pull down": ["To demolish or lower"],
    "Pull in": ["To arrive at a destination or come to a stop"],
    "Pull off": ["To succeed in doing something difficult"],
    "Pull out": ["To withdraw from a place or commitment"],
    "Pull over": ["To move to the side of the road and stop"],
    "Pull through": ["To recover from a serious illness or difficulty"],
    "Pull together": ["To work cooperatively"],
    "Pull up": ["To stop; also, to bring up a topic"],
    "Punch in": ["To clock in or register the time of arrival"],
    "Punch out": ["To clock out or register the time of departure"],
    "Punch up": ["To improve or make more interesting"],
    "Push around": ["To bully or order someone around"],
    "Put across": ["To communicate or express an idea clearly"],
    "Put aside": ["To save or set apart for later"],
    "Put away": ["To put something in the place where you usually keep it"],
    "Put back": ["To return something to its original place"],
    "Put by": ["To save money for future use"],
    "Put down": ["To write information; To stop holding something and place it on the ground"],
    "Put forward": ["To propose or suggest"],
    "Put in": ["To install or submit"],
    "Put off": ["To postpone or delay"],
    "Put on": ["To wear; to deceive; to start a performance"],
    "Put out": ["To extinguish; to inconvenience"],
    "Put past": ["To not be surprised if someone does something unexpected"],
    "Put through": ["To connect a phone call; to cause someone to undergo something often a difficult or unpleasant experience."],
    "Put together": ["To assemble or compile"],
    "Put up": ["To construct or erect something; to display a notice, sign, or poster"],
    "Put up to": ["To encourage or incite someone to do something"],
    "Put up with": ["To tolerate or endure"],
    "Puzzle out": ["To solve a confusing or complicated problem"],
    "Quarrel with": ["To argue or dispute"],
    "Queue up": ["To line up or wait in line"],
    "Quieten down": ["To become quiet or calmer"],
    "Quit on": ["To stop supporting or looking after someone"],
    "Race through": ["To do something very quickly"],
    "Rake over": ["To revisit or talk again about (often unpleasant)"],
    "Rally round/around": ["To come together to support someone"],
    "Ramp up": ["To increase or grow"],
    "Rattle on": ["To talk for a long time that is not important or interesting"],
    "Rattle through": ["To do or say something quickly and efficiently"],
    "Rave on": ["To talk excitedly or wildly"],
    "Reach out": ["To ask for help or offer help"],
    "Read into": ["To infer something not explicitly stated"],
    "Read out": ["To read something and say the words aloud so that other people can hear"],
    "Read up on": ["To research or inform oneself about something"],
    "Rebound from": ["To recover from"],
    "Reckon with": ["To deal with a difficult or powerful person or thing"],
    "Refer to": ["To mention or allude to something"],
    "Reflect on/upon": ["To think deeply about something"],
    "Rely on": ["To depend on someone or something"],
    "Remind of": ["To cause someone to remember something"],
    "Resign yourself to": ["To accept something reluctantly but without protest"],
    "Result in": ["To lead to a particular situation or outcome"],
    "Return to": ["To go back to a place or topic"],
    "Rev up": ["To increase in activity or speed"],
    "Revert to": ["To return to a previous state or condition"],
    "Rig up": ["To assemble or set up hastily with available materials"],
    "Ring back": ["To call (someone or some place) on the telephone again"],
    "Ring off": ["To end a phone call"],
    "Ring up": ["To make a telephone call; also, to tally a total in sales"],
    "Rip into": ["To criticize or verbally attack vigorously"],
    "Rip off": ["To cheat or overcharge; to plagiarize"],
    "Rip up": ["To tear something into pieces"],
    "Roll out": ["To launch or introduce something new"],
    "Roll over": ["To agree to what someone wants; to be easily defeated without even trying"],
    "Root out": ["To eradicate or remove completely"],
    "Rope in": ["To persuade someone to join or participate"],
    "Rough up": ["To treat someone violently"],
    "Round off": ["To complete something in a satisfactory or balanced manner"],
    "Round up": ["To gather together; to increase to the nearest round number"],
    "Rub off on": ["To influence someone by one's own qualities or characteristics"],
    "Rub out": ["To erase; to kill or eliminate"],
    "Rule out": ["Exclude, eliminate"],
    "Run across": ["To find or encounter by chance"],
    "Run after": ["To chase or pursue"],
    "Run against": ["To compete against"],
    "Run around": ["To be very busy doing many things"],
    "Run away": ["To flee or escape"],
    "Run away from": ["To avoid facing a difficult situation"],
    "Run down": ["To criticize; to hit with a vehicle; to become depleted"],
    "Run into": ["To encounter unexpectedly"],
    "Run off": ["To print copies; to flee"],
    "Run on": ["To continue longer than expected"],
    "Run out": ["To use up or exhaust supply"],
    "Run over": ["To exceed a time limit; to hit with a vehicle"],
    "Run short of": ["To not have enough of something"],
    "Run through": ["To rehearse; to pierce; to spend quickly"],
    "Run up": ["To accumulate a large amount; to hoist"],
    "Run up against": ["To encounter difficulties"],
    "Save up": ["To accumulate money for a specific purpose"],
    "Screw on": ["To attach by twisting or turning"],
    "Screw out of": ["To cheat someone out of something"],
    "Screw up": ["To make a mistake or mishandle a situation"],
    "Seal off": ["To isolate or close off an area"],
    "See about": ["To arrange or deal with something"],
    "See off": ["To bid farewell or to dispatch"],
    "See through": ["To perceive the truth; to support till the end"],
    "See to": ["To attend or take care of something"],
    "Sell out": ["To sell the entire stock; to betray"],
    "Send back": ["To return something to its origin"],
    "Send for": ["To request the presence of someone"],
    "Set about": ["To start doing something"],
    "Set apart": ["To distinguish or separate from others"],
    "Set aside": ["To reserve or put something to one side"],
    "Set back": ["To delay or cause to be delayed"],
    "Set down": ["To put in writing; to land (as in an aircraft)"],
    "Set forth": ["To explain or describe in detail; to start a journey"],
    "Set in": ["To begin and seem likely to continue"],
    "Set off": ["To start a journey; to cause to explode"],
    "Set on/upon": ["To attack or to encourage someone to attack"],
    "Set out": ["To begin with a specific goal in mind"],
    "Set to": ["To begin doing something with enthusiasm or determination"],
    "Set up": ["To establish or arrange"],
    "Settle down": ["To become calm or stable in life or a situation"],
    "Settle for": ["To accept something less than desired"],
    "Settle in": ["To become comfortable in a new environment"],
    "Shake off": ["To get rid of something"],
    "Shake up": ["To upset the status quo; to rearrange"],
    "Shoot down": ["To reject or criticize sharply"],
    "Shoot up": ["To increase rapidly; also, to inject drugs"],
    "Shop around": ["To compare prices before buying"],
    "Show off": ["To display boastfully"],
    "Show up": ["To arrive or appear"],
    "Shut down": ["To turn off; to cease operations"],
    "Shut off": ["To stop the flow or operation of something"],
    "Shut out": ["To prevent from entering or being included"],
    "Shut up": ["To stop talking; to silence someone or something"],
    "Sign in": ["To register one's arrival, especially on a computer system"],
    "Sign out": ["To register one's departure, especially from a computer system"],
    "Sign up": ["To enroll or register for something"],
    "Sit back": ["To relax or wait passively"],
    "Sit down": ["To take a seat"],
    "Sit on": ["To delay or postpone action on something"],
    "Sit through": ["To stay until the end of a tedious or long event"],
    "Sit up": ["To rise to a sitting position; to pay close attention"],
    "Sleep over": ["To stay overnight in someone else's home"],
    "Slip up": ["To make a mistake"],
    "Slow down": ["To reduce speed or rate"],
    "Sneak in/into": ["To enter secretly or quietly without being noticed"],
    "Sneak out": ["To leave secretly or quietly without being noticed"],
    "Sort out": ["To organize, resolve a problem, or separate items"],
    "Space out": ["To become distracted or unfocused; to dissociate"],
    "Speak out": ["To express one's opinions openly and frankly"],
    "Speed up": ["To increase speed or rate"],
    "Split up": ["To separate or break up"],
    "Spread out": ["To distribute over a wide area or among a number of people"],
    "Stand around": ["To remain idle in one place"],
    "Stand by": ["To support; to be ready for action"],
    "Stand down": ["To resign from a position of withdraw"],
    "Stand for": ["To represent or signify"],
    "Stand out": ["To be noticeably different of better"],
    "Stand up": ["To rise to an upright position"],
    "Stand up for": ["To defend or support a cause or person"],
    "Start off": ["To begin or start a journey"],
    "Start out": ["To begin one's life, career, or existence in a particular way"],
    "Start up": ["To begin operation or cause to begin operating"],
    "Stay away from": ["To avoid being near or involved with"],
    "Stay off": ["To refrain from using or stepping on"],
    "Stay out": ["To remain outdoors or away from home, especially at night"],
    "Stay up": ["To remain awake, especially later than usual"],
    "Step aside": ["To move out of the way; to resign from a position"],
    "Step down": ["To resign from a high position or responsibility"],
    "Step in": ["To intervene or become involved"],
    "Step on": ["To place one's foot on something; to pressure"],
    "Step out": ["To leave a place for a short time"],
    "Step up": ["To increase or improve; to take action"],
    "Stick around": ["To stay in a place or be nearby"],
    "Stick out": ["To protrude or extend beyond a surface; to be noticeable"],
    "Stick to": ["To adhere to a plan, rule, or decision"],
    "Stick up": ["To rob, especially at gunpoint; to raise"],
    "Stick up for": ["To defend or support"],
    "Stick with": ["To continue with or remain loyal to"],
    "Stop off": ["To make a brief visit somewhere during a journey"],
    "Stop over": ["To stay at a place briefly while on the way to somewhere else"],
    "Storm out": ["To leave angrily"],
    "Straighten out": ["To resolve a problem or misunderstanding"],
    "Stress out": ["To feel very anxious, stressed or overwhelmed"],
    "Strike down": ["To officially annul or invalidate"],
    "Strike off": ["To remove a name or item from a list or record"],
    "Sum up": ["To summarize or give a brief statement"],
    "Switch off": ["To turn off a device or light"],
    "Switch on": ["To turn on a device or light"],
    "Take after": ["To resemble in appearance, behavior, or character"],
    "Take apart": ["To disassemble"],
    "Take away": ["To remove or subtract"],
    "Take back": ["To retract a statement or to accept something/someone back"],
    "Take care of": ["To look after or be responsible for"],
    "Take down": ["To dismantle or note down"],
    "Take for": ["To assume or mistake someone/something for another"],
    "Take in": ["To absorb; to deceive; to make clothes smaller"],
    "Take off": ["To remove; to leave the ground (aircraft); to become successful"],
    "Take on": ["To accept responsibility or work; to compete against"],
    "Take out": ["To remove; to go on a date"],
    "Take out on": ["To unleash one's emotions or frustrations on someone"],
    "Take over": ["To assume control of something"],
    "Take someone over": ["To assume someone is a certain kind of person"],
    "Take to": ["To develop a liking for: to begin to do"],
    "Take up": ["To start a new hobby or challenge: to occupy space or time"],
    "Talk back": ["To reply rudely or defensively"],
    "Talk down to": ["To talk to someone as if they are less intelligent than you"],
    "Talk into": ["To persuade someone to do something"],
    "Talk out": ["To discuss something thoroughly until an agreement is reached"],
    "Talk out of": ["To persuade someone not to do something"],
    "Talk over": ["To discuss something in detail"],
    "Talk to": ["To speak with someone"],
    "Tear apart": ["To destroy or criticize harshly; to upset greatly"],
    "Tear down": ["To demolish or remove"],
    "Tear off": ["To remove by tearing"],
    "Tear up": ["To rip into pieces; to become very emotional"],
    "Tell apart": ["To distinguish between two or more things"],
    "Tell off": ["To scold or reprimand"],
    "Tell on": ["To inform on someone; to have a negative effect"],
    "Tell upon": ["To have a noticeable effect on someone"],
    "Think about": ["To consider"],
    "Think ahead": ["To plan for the future"],
    "Think back": ["To recall or remember"],
    "Think of": ["To consider or have an opinion about something"],
    "Think over": ["To consider carefully before making a decision"],
    "Think up": ["To invent or imagine something"],
    "Throw away": ["To discard; to waste"],
    "Throw out": ["To discard; to eject from a place"],
    "Throw up": ["To vomit; to give up or abandon"],
    "Tidy up": ["To clean or organize"],
    "Tie up": ["To bind or secure with a rope or cord; to engage or occupy"],
    "Tone down": ["To make something less forceful or offensive"],
    "Touch on": ["To mention or refer to something briefly"],
    "Touch up": ["To improve or repair small details"],
    "Toy with": ["To consider something casually or without seriousness"],
    "Track down": ["To find something or someone after a search"],
    "Trade in": ["To exchange something as part of a transaction for something else"],
    "Trick into": ["To deceive someone into doing something"],
    "Try on": ["To wear something to see if it fits or looks good"],
    "Try out": ["To test or use something to see if it works or is suitable"],
    "Turn around": ["To change direction; to improve significantly"],
    "Turn away": ["To refuse entry or service"],
    "Turn back": ["To return to a starting point; to revert"],
    "Turn down": ["To refuse or reject an offer or request"],
    "Turn in": ["To submit; to go to bed"],
    "Turn into": ["To transform into something else"],
    "Turn off": ["To deactivate or stop a device or light"],
    "Turn on": ["To activate or start a device or light; to excite or interest"],
    "Turn out": ["To develop or result; to attend or produce"],
    "Turn over": ["To flip; to transfer control or possession"],
    "Turn up": ["To arrive unexpectedly; to increase volume or intensity"],
    "Urge on": ["To encourage or motivate strongly"],
    "Use up": ["To consume or deplete entirely"],
    "Verge on": ["To approach closely; to be on the edge of"],
    "Vote in": ["To elect into office or accept by voting"],
    "Vote off": ["To remove from consideration or participation by voting"],
    "Vouch for": ["To confirm the truth or reliability of someone or something"],
    "Wait around": ["To remain in one place waiting for someone or something"],
    "Wait on": ["To serve or attend to someone"],
    "Wake up": ["To arise from sleep; to awaken someone"],
    "Walk out": ["To leave a place in protest or as part of a strike"],
    "Ward off": ["To avert or prevent something"],
    "Warm up": ["To prepare for physical exertion or a performance by exercising lightly"],
    "Wash away": ["To remove or carry off by the action of water"],
    "Wash off": ["To clean something by washing"],
    "Wash out": ["To be removed by washing; to cancel due to bad weather"],
    "Wash up": ["To clean the dishes, utensils, etc., after a meal, to wash one's face and hands"],
    "Watch out": ["To be cautious or alert to danger"],
    "Watch out for": ["To be vigilant or look carefully for something or someone"],
    "Wear down": ["To exhaust or become exhausted; to erode"],
    "Wear off": ["To diminish in effect"],
    "Wear out": ["To cause to become tired, weary or fatigued"],
    "Weed out": ["To remove or eliminate unwanted parts or members"],
    "Weigh down": ["To burden someone with worries, responsibilities, or problems"],
    "Weigh up": ["To consider and assess"],
    "While away": ["To spend time in a relaxed manner or doing nothing"],
    "Win back": ["To regain something lost"],
    "Wind up": ["To conclude or end something"],
    "Wipe away": ["To remove completely, often marks or memories"],
    "Wipe off": ["To clean a surface by rubbing"],
    "Wipe out": ["To destroy or erase completely"],
    "Wipe up": ["To clean or absorb liquid"],
    "Work at/on": ["To be engaged in or make an effort towards a task"],
    "Work in": ["To incorporate or find time for something in a schedule"],
    "Work out": ["To exercise; to solve a problem"],
    "Work up": ["To develop or produce, to gradually bring someone to a state of intense excitement, anger, or anxiety."],
    "Wrap up": ["To conclude or finish something"],
    "Write off": ["To cancel or deem as a loss"],
    "Yearn for": ["To have a strong desire or longing for"],
    "Yell out": ["To shout or say something loudly"],
    "Zero in on": ["To focus or concentrate on"],
    "Zip up": ["To fasten or close with a zipper"],
    "Zonked out": ["To be completely exhausted or asleep"],
    "Zoom in": ["To focus more closely something, to adjust a camera to make person or thing being photographed appear larger or closer"]
}

MM_IDIOMS_DATA = {
  "A bird in the hand is worth two in the bush": [
    "Having something certain is better than the possibility of getting something better."
  ],
  "A bird\"s eye view": [
    "A general view from above."
  ],
  "A blessing/boon in disguise": [
    "An apparent misfortune that eventually has good results."
  ],
  "A blue-eyed boy": [
    "One who is favourite."
  ],
  "A bolt from the blue": [
    "Something unexpected and unpleasant."
  ],
  "A bone of contention": [
    "A cause of dispute or quarrel."
  ],
  "A bull in a China shop": [
    "A clumsy person in a delicate situation."
  ],
  "A cakewalk": [
    "An easy achievement or victory."
  ],
  "A carrot and stick approach": [
    "Rewards and punishments that influence someone’s behaviour."
  ],
  "A change of heart": [
    "A change in one’s opinion or feelings."
  ],
  "A close-fisted person": [
    "A miser."
  ],
  "A cold fish": [
    "Someone who seems unfriendly and who does not share his feelings."
  ],
  "A cut above something": [
    "Superior to."
  ],
  "A damp squib": [
    "A disappointing result or situation less impressive than expected."
  ],
  "A dark horse": [
    "An unexpected winner or competitor of unknown capabilities."
  ],
  "A dime a dozen": [
    "Very common and easily obtainable."
  ],
  "A dog’s life": [
    "A miserable existence."
  ],
  "A drop in a bucket": [
    "A very small part too insignificant to matter."
  ],
  "A dry run": [
    "A rehearsal or practice session."
  ],
  "A fire in someone’s belly": [
    "One who is energetic and enthusiastic about something."
  ],
  "A fish out of water": [
    "A person in an unfamiliar or uncomfortable environment."
  ],
  "A flying visit": [
    "A very short visit."
  ],
  "A fool’s paradise": [
    "A state of happiness based on ignorance of potential trouble."
  ],
  "A gentleman at large": [
    "A man without a job."
  ],
  "A golden mean": [
    "Middle course between two extremes; neither too much nor too little."
  ],
  "A green horn": [
    "An inexperienced man."
  ],
  "A grey area": [
    "An unclear or undefined situation."
  ],
  "A hairbreadth escape": [
    "A narrow escape."
  ],
  "A hard nut to crack": [
    "A tough challenge or difficult person."
  ],
  "A hornet’s nest": [
    "An unpleasant, difficult, or troublesome situation."
  ],
  "A hot potato": [
    "A controversial or difficult issue."
  ],
  "A house of cards": [
    "A fragile or unstable situation that can easily collapse."
  ],
  "A kick in the teeth": [
    "A grave setback or great disappointment."
  ],
  "A lame excuse": [
    "A weak or unsatisfactory explanation."
  ],
  "A laughing stock": [
    "An object of ridicule or laughter."
  ],
  "A left handed compliment": [
    "An ambiguous compliment that may be insulting."
  ],
  "A leopard can’t change its spots": [
    "It is impossible for one to change one’s character."
  ],
  "A little bird told me": [
    "To receive information from a secret source without naming it."
  ],
  "A live wire": [
    "A person who is full of energy."
  ],
  "A lot on your plate": [
    "Having many responsibilities or problems to deal with."
  ],
  "A man of letters": [
    "A scholar; someone proficient in literary art."
  ],
  "A man of straw": [
    "A man of no substance; a weak or cowardly person."
  ],
  "A mare’s nest": [
    "A complicated situation or false invention."
  ],
  "A needle in a haystack": [
    "Something very difficult to locate or attempt."
  ],
  "A pain in the neck": [
    "Something or someone that is annoying or a nuisance."
  ],
  "A Penelope’s web": [
    "An endless, never-ending job."
  ],
  "A penny for your thoughts": [
    "A way of asking what someone is thinking."
  ],
  "A picture paints a thousand words": [
    "An image conveying meaning more effectively than description."
  ],
  "A piece of cake": [
    "A very easy task."
  ],
  "A plum job": [
    "An easy, pleasant job that pays well."
  ],
  "A queer fish": [
    "An eccentric or unconventional person."
  ],
  "A red letter day": [
    "An important or memorable day."
  ],
  "A red rag to a bull": [
    "An act certain to provoke someone."
  ],
  "A rolling stone gathers no moss": [
    "A person who does not settle in one place and therefore gains no advantage."
  ],
  "A rotten apple": [
    "A single bad person in a group."
  ],
  "A safe pair of hands": [
    "A reliable person who can be trusted to do something efficiently."
  ],
  "A sea change": [
    "A profound or notable transformation."
  ],
  "A shot in the arm": [
    "Something that gives encouragement."
  ],
  "A skeleton in the cupboard": [
    "An embarrassing fact or shameful secret to be kept hidden."
  ],
  "A square deal": [
    "A fair and honest agreement."
  ],
  "A stitch in time saves nine": [
    "Fixing a problem promptly prevents it from worsening."
  ],
  "A stone’s throw away": [
    "A very short distance."
  ],
  "A storm in a teacup": [
    "A big fuss or excitement about a trivial matter."
  ],
  "A thorn in the flesh": [
    "A source of continual annoyance or trouble."
  ],
  "A turning point": [
    "A time when an important change begins."
  ],
  "A wet blanket": [
    "A person who discourages enjoyment or enthusiasm."
  ],
  "A wolf in sheep’s clothing": [
    "A dangerous person pretending to be harmless."
  ],
  "Above board": [
    "Honest and frank; without any secret."
  ],
  "Above/Over one’s head": [
    "Beyond one’s capability to understand something."
  ],
  "Achilles’ heel": [
    "A weakness or vulnerable point."
  ],
  "Acid test": [
    "Definitive proof of truth or falsehood."
  ],
  "Actions speak louder than words": [
    "What you do is more important than what you say; intentions judged by actions."
  ],
  "Add fuel to the fire/flames": [
    "Make a bad situation worse."
  ],
  "Add insult to injury": [
    "To further a loss with mockery, making a bad situation even worse."
  ],
  "After one’s own heart": [
    "Having likes and dislikes similar to one’s own."
  ],
  "Against the clock": [
    "Work very fast to complete something within a deadline."
  ],
  "Alive and kicking": [
    "In good health."
  ],
  "All agog": [
    "Amazed or full of interest and excitement."
  ],
  "All and sundry": [
    "Everybody without distinction; all included."
  ],
  "All at sea": [
    "Puzzled; in a state of confusion or lost."
  ],
  "All eyes": [
    "Watching eagerly; to watch something intently."
  ],
  "All eyes and ears": [
    "To be attentive and fully focused on something."
  ],
  "All moonshine": [
    "Nonsense; far from reality or concocted."
  ],
  "All our might and main": [
    "Exercising full force; with all one’s strength and energy."
  ],
  "All thumbs": [
    "Clumsy; physically awkward."
  ],
  "Alpha and omega": [
    "The beginning and the end; everything."
  ],
  "Alphabet soup": [
    "A confusing jumble of abbreviations or acronyms."
  ],
  "An eye opener": [
    "A shocking revelation."
  ],
  "An iron hand": [
    "Strict and harsh control."
  ],
  "An iron will": [
    "A firm opinion; strong determination."
  ],
  "An open book": [
    "Someone or something with no secrets; fully transparent."
  ],
  "Apple of discord": [
    "The cause of a quarrel or animosity."
  ],
  "Apple of one’s eye": [
    "Someone very precious or dearly loved."
  ],
  "Apples and oranges": [
    "Unequal comparisons between two unlike things."
  ],
  "Argus-eyed": [
    "Carefully observant and attentive; vigilant."
  ],
  "Armed to the teeth": [
    "Heavily armed or fortified."
  ],
  "Around the corner": [
    "Happening very soon; occurring shortly."
  ],
  "As daft as a brush": [
    "Extremely silly or foolish."
  ],
  "As fit as a fiddle": [
    "Strong, healthy, in top condition."
  ],
  "As hard as a nail": [
    "Emotionless or unrelenting; having no feelings."
  ],
  "As the crow flies": [
    "By the shortest, direct route in a straight line."
  ],
  "At a crossroads": [
    "A point in life where decisions will have long-term consequences."
  ],
  "At a snail’s pace": [
    "Doing something very slowly."
  ],
  "At beck and call": [
    "Always available to help; at one’s disposal."
  ],
  "At cross purposes": [
    "Having opposing viewpoints or intentions; misunderstanding each other."
  ],
  "At daggers drawn": [
    "To be bitterly hostile or open enemies."
  ],
  "At large": [
    "A criminal who has escaped or is not yet captured."
  ],
  "At loggerheads": [
    "In conflict with someone; to disagree strongly."
  ],
  "At loose ends": [
    "In an uncertain or unsettled situation."
  ],
  "At one’s wits’ end": [
    "Completely confused or perplexed."
  ],
  "At sixes and sevens": [
    "In disorder or confusion."
  ],
  "At the drop of a hat/dime": [
    "Without any hesitation; instantly or without planning."
  ],
  "At the eleventh hour": [
    "At the very last moment; just before the deadline."
  ],
  "Back out of": [
    "Withdraw from a commitment."
  ],
  "Back to square one": [
    "Return to the starting point; having to start all over again."
  ],
  "Back to the drawing board": [
    "An idea has failed and must be redesigned."
  ],
  "Back up": [
    "Defend or support."
  ],
  "Backseat driver": [
    "Interfering in affairs without authority; someone who offers unsolicited advice."
  ],
  "Bad blood": [
    "Angry feeling or enmity between people."
  ],
  "Bag and baggage": [
    "With all one’s belongings; with full luggage."
  ],
  "Baker’s dozen": [
    "A group of 13 items; one more than a usual dozen."
  ],
  "Ball is in your court": [
    "It is up to you to make the next decision or be responsible for further action."
  ],
  "Barking up the wrong tree": [
    "Trying to do something in a way that will not work or accusing the wrong person."
  ],
  "Be all ears": [
    "Listening intently; eager to hear."
  ],
  "Be behind the times": [
    "Outdated or old-fashioned."
  ],
  "Be glad to see the back of": [
    "Feel happy when someone or something leaves."
  ],
  "Be going places": [
    "To be talented and likely to succeed."
  ],
  "Be hard up": [
    "To be very short of money."
  ],
  "Be in the red": [
    "To be in debt or losing money."
  ],
  "Be in two minds": [
    "Unable to decide; holding conflicting opinions."
  ],
  "Be like chalk and cheese": [
    "To be completely different from each other."
  ],
  "Be out for the count": [
    "To be unconscious or in deep sleep."
  ],
  "Be out of order": [
    "An object or device not working properly."
  ],
  "Be under somebody’s thumb": [
    "To be completely controlled or dominated by someone."
  ],
  "Be wet behind the ears": [
    "To be inexperienced or naive."
  ],
  "Bear a grudge": [
    "To hold resentment or feel anger against someone for a past incident."
  ],
  "Bear fruit": [
    "To yield positive results."
  ],
  "Bear the brunt of": [
    "To suffer the worst of something; to endure the maximum impact."
  ],
  "Bear the palm": [
    "Win or be declared the victor."
  ],
  "Bear up with": [
    "Endure a difficult situation; be strong enough to continue."
  ],
  "Beat about/around the bush": [
    "Speak vaguely or avoid the main topic."
  ],
  "Bed of roses": [
    "A comfortable, pleasant situation or life."
  ],
  "Behind closed doors": [
    "Do something secretly."
  ],
  "Behind one’s back": [
    "In someone’s absence; without their knowledge."
  ],
  "Behind the eight ball": [
    "In a difficult or disadvantaged position."
  ],
  "Behind the scenes": [
    "Secretly or out of public view."
  ],
  "Bell the cat": [
    "Do the impossible or most dangerous job."
  ],
  "Below the belt": [
    "A cruel or unfair action."
  ],
  "Bend over backwards": [
    "Try very hard to accommodate or please someone."
  ],
  "Beside oneself": [
    "Almost out of one’s senses with emotion."
  ],
  "Beside the mark": [
    "Irrelevant or not applicable."
  ],
  "Best of both worlds": [
    "A situation offering two different advantages simultaneously."
  ],
  "Best thing since sliced bread": [
    "A truly remarkable innovation or idea."
  ],
  "Better late than never": [
    "It is better to arrive late than not to come at all."
  ],
  "Between a rock and a hard place": [
    "Stuck between two very bad options."
  ],
  "Between Scylla and Charybdis": [
    "Choice between two equally unpleasant alternatives."
  ],
  "Between the devil and the deep blue sea": [
    "Stuck between two very bad options."
  ],
  "Beyond the pale": [
    "Unacceptable or unreasonable."
  ],
  "Bid defiance": [
    "To offer resistance; disregard recklessly."
  ],
  "Birds of the same feather": [
    "Two people of the same character or interests."
  ],
  "Bite off more than one can chew": [
    "Take on more responsibility than one can handle."
  ],
  "Bite someone’s head off": [
    "Speak angrily without any reason."
  ],
  "Bite the bullet": [
    "To force yourself to do something unpleasant because inevitable."
  ],
  "Bite the dust": [
    "Suffer a defeat; die."
  ],
  "Bite your tongue": [
    "Stop yourself from saying something."
  ],
  "Black and blue": [
    "Describe someone badly bruised or to beat mercilessly."
  ],
  "Black sheep": [
    "A single bad person in a group because of bad conduct."
  ],
  "Blaze a trail": [
    "Lead the way as a pioneer; initiate something new."
  ],
  "Blow one’s own trumpet": [
    "Praise oneself; talk boastfully about one’s achievements."
  ],
  "Blue-blooded": [
    "Of noble birth."
  ],
  "Body and soul": [
    "With all your energy."
  ],
  "Boil the ocean": [
    "Undertaking an impossible chore or task."
  ],
  "Bone to pick": [
    "Cause of quarrel; to be angry about something and want to discuss it."
  ],
  "Born with a silver spoon in one’s mouth": [
    "To be born into a wealthy, privileged family."
  ],
  "Bread and butter": [
    "The means of livelihood; main source of income."
  ],
  "Break a leg": [
    "To wish someone good luck or to perform well."
  ],
  "Break in": [
    "To force entry into a building illegally."
  ],
  "Break new/fresh ground": [
    "To innovate; to do or discover something new."
  ],
  "Break the bank": [
    "To be very expensive or to win more money than is held by the bank."
  ],
  "Break the ice": [
    "To initiate a conversation or to break a painful silence and make someone comfortable."
  ],
  "Breathing down someone’s neck": [
    "Watching all someone’s actions closely; monitoring them."
  ],
  "Bring about": [
    "Cause to happen."
  ],
  "Bring home the bacon": [
    "To be successful; to earn a living."
  ],
  "Bring someone to book": [
    "To punish someone for wrongdoing or hold them accountable."
  ],
  "Bring the house down": [
    "To make an audience applaud enthusiastically."
  ],
  "Broke down": [
    "Wept bitterly; cried."
  ],
  "Broken reed": [
    "A weak person; support that failed."
  ],
  "Build castles in the air": [
    "To have unrealistic ideas or dreams."
  ],
  "Bull’s-eye": [
    "The centre of a target; a perfect hit."
  ],
  "Burn one’s bridges/boats": [
    "To destroy all relations or make return impossible."
  ],
  "Burn the midnight oil": [
    "To work or study very late at night."
  ],
  "Burning question": [
    "An important, pressing question or issue."
  ],
  "Bury the hatchet": [
    "To make peace; end a quarrel."
  ],
  "Butterflies in the stomach": [
    "To be anxious and nervous."
  ],
  "By and by": [
    "Gradually; after a while."
  ],
  "By and large": [
    "In general; on the whole."
  ],
  "By courtesy of": [
    "Given or allowed by; with kindly consideration."
  ],
  "By fair means or foul": [
    "In any way, by honest or dishonest methods."
  ],
  "By fits and starts": [
    "Unsteadily; irregularly."
  ],
  "By hook or by crook": [
    "By any means, good or bad; using whatever methods."
  ],
  "By leaps and bounds": [
    "Very quickly; rapidly; swiftly."
  ],
  "By the skin of one’s teeth": [
    "By the narrowest margin; barely manage to achieve something."
  ],
  "Call in question": [
    "To challenge; dispute something."
  ],
  "Call it a day": [
    "To decide to stop doing something and go home."
  ],
  "Call on": [
    "To pay a visit."
  ],
  "Call the shots": [
    "To be in control; to make decisions."
  ],
  "Called for": [
    "To require something; to demand."
  ],
  "Can’t cut the mustard": [
    "To be unable to do a job; not measure up."
  ],
  "Carry out": [
    "To execute or complete something."
  ],
  "Carry the day": [
    "To win a victory; emerge as the winner."
  ],
  "Cat nap": [
    "To have disturbed sleep; a brief sleep."
  ],
  "Catch 22": [
    "A particular situation in which one cannot do anything."
  ],
  "Catch a tartar": [
    "To catch someone unexpectedly powerful or troublesome."
  ],
  "Catch red-handed": [
    "To catch someone doing something illegal; in the act of committing a crime."
  ],
  "Change hands": [
    "Pass from one person to another; change of ownership."
  ],
  "Chapter and verse": [
    "To give exact information or minute details."
  ],
  "Charley horse": [
    "A cramp in a muscle."
  ],
  "Cheek by jowl": [
    "Very close together."
  ],
  "Chew the cud": [
    "To think slowly and carefully about something."
  ],
  "Chew the fat": [
    "Gossip and make small talk; have friendly talks."
  ],
  "Chew the scenery": [
    "To act over-dramatically."
  ],
  "Chicken out": [
    "To decide not to do something because you are too frightened; withdraw."
  ],
  "Chicken-hearted": [
    "Cowardly; easily frightened."
  ],
  "Child’s play": [
    "Something very easy to do; a very easy task."
  ],
  "Chill out": [
    "To calm down."
  ],
  "Chinks in the armour": [
    "Small flaws or weaknesses."
  ],
  "Chip off the old block": [
    "Resembling one’s father in character or behaviour."
  ],
  "Cloak and dagger": [
    "An activity involving secrecy and mystery."
  ],
  "Close shave": [
    "A narrow escape from danger or disaster."
  ],
  "Cock and bull story": [
    "An unbelievable or absurd story."
  ],
  "Cold comfort": [
    "Slight satisfaction; little consolation."
  ],
  "Come hell or high water": [
    "In spite of any obstacles; no matter what."
  ],
  "Come in handy": [
    "To turn out to be useful."
  ],
  "Come of age": [
    "To mature and develop fully."
  ],
  "Come rain or shine": [
    "Under any circumstances; whatever the weather."
  ],
  "Come to blows": [
    "To get into a physical fight."
  ],
  "Come to light": [
    "To be revealed; become known publicly."
  ],
  "Come what may": [
    "No matter what happens."
  ],
  "Cook the books": [
    "To falsify financial records; dishonest accounting."
  ],
  "Cool as a cucumber": [
    "Not nervous or emotional; calm and composed."
  ],
  "Cool your heels": [
    "To be kept waiting; unwillingly wait for something or someone."
  ],
  "Cost an arm and a leg": [
    "To be very expensive; a large amount of money."
  ],
  "Couch potato": [
    "A person who watches too much television; a lazy person."
  ],
  "Crack someone up": [
    "Laugh out loud; to make someone laugh."
  ],
  "Cross one’s mind": [
    "To think of something; to be thought of by one."
  ],
  "Cross swords": [
    "To disagree; to fight."
  ],
  "Cross that bridge when you come to it": [
    "To deal with a problem only when it arises."
  ],
  "Cross your fingers": [
    "To hope that things will happen the way you want them to; to wish for good luck or success."
  ],
  "Crux of the matter": [
    "The most important or critical point."
  ],
  "Cry for the moon": [
    "To make an impractical, unreasonable request; to aspire to the impossible."
  ],
  "Cry in the wilderness": [
    "An unrealistic demand; an unheeded warning."
  ],
  "Cry over spilt milk": [
    "To complain about a loss from the past; feeling sorry over a mistake that cannot be changed."
  ],
  "Cup of tea": [
    "One’s chosen or preferred thing; something that pleases one."
  ],
  "Currying favour with": [
    "Behaving obsequiously to ingratiate oneself with someone."
  ],
  "Cut and dried": [
    "Ready made; already decided."
  ],
  "Cuts corners": [
    "To save money, time, or effort by omitting necessary parts."
  ],
  "Cut no ice with me": [
    "Had no influence on me."
  ],
  "Cut one short": [
    "To interrupt someone."
  ],
  "Cut someone some slack": [
    "Not to criticize too strictly; to be more lenient."
  ],
  "Cut the Gordian knot": [
    "Solve a complex problem by a bold stroke; remove the difficulty."
  ],
  "Cut the mustard": [
    "To perform well; to succeed."
  ],
  "Cut to the chase": [
    "To come to the point; get to the important matters."
  ],
  "Cut to the quick": [
    "Hurt intensely; deeply offend."
  ],
  "Dance to someone’s tune": [
    "Do what others want you to do."
  ],
  "Dead ringer": [
    "An exact duplicate."
  ],
  "Desperate times call for desperate measures": [
    "When you are extremely desperate you need extremely drastic actions."
  ],
  "Died in harness": [
    "Worked or served until death."
  ],
  "Do a good turn": [
    "Render a service; help someone."
  ],
  "Don’t (or never) judge a book by its cover": [
    "We should not judge something by its outward appearance."
  ],
  "Done for": [
    "Ruined; beyond help."
  ],
  "Donkey’s years": [
    "A very long time."
  ],
  "Don’t count your chickens before they hatch": [
    "Don’t make plans based on events that have not yet happened."
  ],
  "Don’t put all your eggs in one basket": [
    "Don’t rely on just one plan or resource."
  ],
  "Dot one’s i’s and cross one’s t’s": [
    "Be detailed and exact; pay attention to every minor point."
  ],
  "Down in the dumps": [
    "Sad and depressed."
  ],
  "Down the drain": [
    "Wasted or lost."
  ],
  "Down to earth": [
    "Practical and sensible."
  ],
  "Drag one’s feet": [
    "To be reluctant to act; do something deliberately at a slow pace."
  ],
  "Draw a blank": [
    "Fail to find or obtain anything; come up with nothing."
  ],
  "Draw a line": [
    "To fix a limit; accept something only up to a certain point."
  ],
  "Drew on his fancy": [
    "To use one’s imagination; draw upon creative powers."
  ],
  "Drive home": [
    "To emphasize or make something clearly understood."
  ],
  "Drive someone up the wall": [
    "To make someone very irritated or angry."
  ],
  "Drop names": [
    "To name‐drop; hint at high connections by mentioning famous people."
  ],
  "Dropping like flies": [
    "Collapsing in large numbers; a great many people or things falling ill or dying."
  ],
  "Eagle eye": [
    "An eye with sharp visual power; a careful or close watcher."
  ],
  "Easier said than done": [
    "More easily talked about than actually accomplished."
  ],
  "Eat anyone’s salt": [
    "To be one’s guest; enjoy someone’s hospitality."
  ],
  "Eats like a horse": [
    "To eat a lot of food."
  ],
  "Egg on": [
    "To encourage or provoke someone."
  ],
  "Elbow grease": [
    "A lot of physical effort; hard manual work."
  ],
  "Elbow room": [
    "Freedom to act; enough space to move or operate."
  ],
  "Ended in a fiasco": [
    "A complete failure."
  ],
  "Every cloud has a silver lining": [
    "Every unpleasant situation has a positive side."
  ],
  "Every dog has his day": [
    "Everyone enjoys success or good luck at some point."
  ],
  "Eye wash": [
    "A deception or pretence."
  ],
  "Face the music": [
    "To accept punishment for a mistake; bear the consequences."
  ],
  "Fair weather friends": [
    "Friends who are supportive in good times only; convenient allies."
  ],
  "Fall back on": [
    "To resort to something; seek support out of necessity."
  ],
  "Fall flat": [
    "To fail to produce the intended effect; have no impact."
  ],
  "Fallout": [
    "To quarrel; stop being friendly after an argument."
  ],
  "Far cry from": [
    "To be very different from; nothing like."
  ],
  "Feather in one’s cap": [
    "An accomplishment to be proud of."
  ],
  "Feather one’s own nest": [
    "To enrich oneself improperly; profit by dishonest means."
  ],
  "Fed up": [
    "Annoyed; irritated."
  ],
  "Feel the pinch": [
    "Have financial problems all of a sudden."
  ],
  "Few and far between": [
    "Rare or seldom seen; not frequent or usual."
  ],
  "Fight shy of": [
    "To avoid encountering."
  ],
  "Finding their feet": [
    "Beginning to understand the work and feeling confident."
  ],
  "First and foremost": [
    "Highest priority; the most important aspect."
  ],
  "Flash in the pan": [
    "Something whose success is short-lived and unlikely to be repeated."
  ],
  "Flying off the handle": [
    "To lose one’s temper suddenly; become enraged."
  ],
  "Follow suit": [
    "To imitate what others have done."
  ],
  "Foot the bill": [
    "To pay for something; pay the cost."
  ],
  "Forty winks": [
    "A short nap or sleep during the day."
  ],
  "Fought to the bitter end": [
    "Carried on regardless of the consequences."
  ],
  "From rags to riches": [
    "To go from very poor to very wealthy."
  ],
  "From the bottom of my heart": [
    "Sincerely; with genuine feeling."
  ],
  "Full of beans": [
    "Lively and energetic; full of energy."
  ],
  "Full of hot air": [
    "Merely loud and angry words but ineffectual."
  ],
  "Gall and wormwood": [
    "To feel hatred or bitterness; something extremely unpleasant."
  ],
  "Gave the game away": [
    "To leak or reveal a secret unintentionally."
  ],
  "Gave vent to something": [
    "To express something forcefully; to let feelings out."
  ],
  "Get a foot in the door": [
    "To gain an initial advantage or entry into a position."
  ],
  "Get a second wind": [
    "To have a burst of renewed energy after fatigue."
  ],
  "Get a taste of your own medicine": [
    "To be given the same (bad) treatment that you have given to others."
  ],
  "Get down to brass tacks": [
    "To start discussing only the important facts of a situation."
  ],
  "Get into hot water": [
    "To get into trouble; to be in a difficult situation in which you can be criticised."
  ],
  "Get on like a house on fire": [
    "To become friends very quickly."
  ],
  "Get on somebody’s nerves": [
    "To irritate or annoy someone."
  ],
  "Get out of hand": [
    "To become uncontrollable; to get out of control."
  ],
  "Get someone’s goat": [
    "To irritate someone."
  ],
  "Get something off one’s chest": [
    "To express something that has been worrying you; get it out in the open."
  ],
  "Get the axe": [
    "To lose one’s job; be fired."
  ],
  "Get the hang of": [
    "To learn how to use; to grasp the main idea."
  ],
  "Get the sack": [
    "To be dismissed; lose one’s job."
  ],
  "Get up on the wrong side of the bed": [
    "To wake up in a bad mood that persists all day."
  ],
  "Get wind of something": [
    "To hear about something; come to know."
  ],
  "Get your act together": [
    "To organize your work in a better way; get oneself under control."
  ],
  "Getting a new lease of life": [
    "A chance to continue living or to become successful or popular again; regain energy."
  ],
  "Gift of the gab": [
    "Ability to speak eloquently and persuasively; a talent for talking."
  ],
  "Give a free hand": [
    "To exercise complete control over something; have full freedom of action."
  ],
  "Give a piece of one’s mind": [
    "To rebuke someone sharply; scold."
  ],
  "Give a wide berth to": [
    "To stay well away from; avoid."
  ],
  "Give and take": [
    "Adjustment; mutual concessions."
  ],
  "Give in": [
    "To yield or surrender."
  ],
  "Give it a shot/whirl": [
    "To try out something; have a go."
  ],
  "Give me a hand with": [
    "To assist; help someone."
  ],
  "Give oneself airs": [
    "To pretend to be superior; act haughty."
  ],
  "Give someone the cold shoulder": [
    "To ignore someone deliberately; be unfriendly."
  ],
  "Give someone the slip": [
    "To escape from someone; elude."
  ],
  "Give the benefit of the doubt": [
    "To accept someone as innocent until proven guilty."
  ],
  "Give up the ghost": [
    "To collapse or die; to cease functioning."
  ],
  "Go against the grain": [
    "To act in a way contrary to one’s natural inclination or values."
  ],
  "Go belly up": [
    "To go bankrupt; fail completely."
  ],
  "Go cold turkey": [
    "To quit an addictive habit abruptly and completely."
  ],
  "Go down in flames": [
    "To fail completely; fail miserably."
  ],
  "Go down like a lead balloon": [
    "To be received badly by an audience."
  ],
  "Go for a song": [
    "To be sold cheaply."
  ],
  "Go for the jugular": [
    "To attack in the most aggressive way; go all out."
  ],
  "Go-getter": [
    "A real achiever; an ambitious, energetic person."
  ],
  "Go the extra mile": [
    "To exceed expectations; make an extra effort."
  ],
  "Go through fire and water": [
    "To experience many dangers in order to achieve something."
  ],
  "Go through the roof": [
    "To rise very high."
  ],
  "Go to rack and ruin": [
    "To be ruined or deteriorate shockingly."
  ],
  "Go to the dogs": [
    "To be ruined or fall into a very poor state."
  ],
  "Go to the wall": [
    "To be ruined; to fail completely."
  ],
  "Go/start with a bang": [
    "To begin in a very exciting and successful way."
  ],
  "God’s ape": [
    "A born fool."
  ],
  "Got the green light": [
    "To receive permission to go ahead with something."
  ],
  "Grasp at straws": [
    "To make a desperate attempt to succeed when nothing else will work."
  ],
  "Grease the palm": [
    "To bribe someone discreetly."
  ],
  "Great minds think alike": [
    "Said when two people make the same choice or have the same idea."
  ],
  "Green thumb": [
    "A person with a natural talent for gardening."
  ],
  "Green-eyed": [
    "Full of envy; jealous."
  ],
  "Grist to the mill": [
    "Something which provides useful advantage; turns to one’s benefit."
  ],
  "Halcyon days": [
    "A time of peace and happiness; idyllic prosperity."
  ],
  "Hale and hearty": [
    "Strong and healthy."
  ],
  "Hand in glove": [
    "In a very close association or partnership; working together intimately."
  ],
  "Hand over fist": [
    "Quickly and continuously (often of earning or losing money)."
  ],
  "Hang in there": [
    "Don’t give up; persist in a difficult situation."
  ],
  "Hang up one’s boots": [
    "To retire from a sport or profession; stop doing it."
  ],
  "Hanging by a thread": [
    "To be in a dangerous or precarious situation."
  ],
  "Hard and fast": [
    "That cannot be altered; strict and fixed."
  ],
  "Hard of hearing": [
    "Partially deaf; having difficulty hearing."
  ],
  "Haste makes waste": [
    "Doing things in a hurry results in poor outcomes."
  ],
  "Haul over the coals": [
    "To scold someone severely for an error."
  ],
  "Have a bee in her bonnet": [
    "To talk and think a lot; to be obsessed with something."
  ],
  "Have a chip on one’s shoulder": [
    "To be upset about something in the past; to harbor a grudge."
  ],
  "Have a finger in every pie": [
    "To be involved in many varied activities or enterprises."
  ],
  "Have a whale of a time": [
    "To have an exceptionally fun or exciting experience."
  ],
  "Have an axe to grind": [
    "To have a private interest or ulterior motive."
  ],
  "Have bigger fish to fry": [
    "To have more important work to attend to."
  ],
  "Have green fingers": [
    "To be naturally gifted at gardening."
  ],
  "Have one’s hands full": [
    "To be very busy; have too much to do."
  ],
  "Have one’s heart in one’s mouth": [
    "To be extremely frightened and nervous."
  ],
  "Have your back to/against the wall": [
    "To be in a desperate situation with very few options."
  ],
  "Head in the clouds": [
    "Daydreaming; being absent-minded."
  ],
  "Head over heels": [
    "Madly in love; completely enamored."
  ],
  "Heads will roll": [
    "Those responsible will be punished or dismissed."
  ],
  "Heart and soul": [
    "Completely; with all the effort you can put in."
  ],
  "Heart to heart talk": [
    "Frank, candid discussion."
  ],
  "Helter-skelter": [
    "In disorderly haste; here and there."
  ],
  "Herculean task": [
    "A very difficult, demanding task."
  ],
  "High and dry": [
    "Neglected; abandoned in a difficult situation."
  ],
  "High and mighty": [
    "Arrogant; puffed up with pride."
  ],
  "High time": [
    "Past the appropriate or proper time; overdue."
  ],
  "Hit a bad patch": [
    "To experience difficulty; go through a rough period."
  ],
  "Hit a brick wall": [
    "To be unable to make any progress; encounter an obstacle."
  ],
  "Hit the books": [
    "To study very hard."
  ],
  "Hit the ceiling/roof": [
    "To explode in anger; lose one’s temper."
  ],
  "Hit the jackpot": [
    "To make money quickly; to find exactly what was sought."
  ],
  "Hold one’s tongue": [
    "To be silent; to keep quiet."
  ],
  "Hold out an olive branch": [
    "To make a peace offering; to show a desire to end a disagreement."
  ],
  "Hold the fort": [
    "To take temporary responsibility for a situation."
  ],
  "Hold water": [
    "To appear acceptable or reasonable; remain valid."
  ],
  "Hold your horses": [
    "To be patient; to wait."
  ],
  "Hope against hope": [
    "To nurture an impossible hope; expect success despite little chance."
  ],
  "Hue and cry": [
    "A noisy expression of protest or anger; loud clamour."
  ],
  "I can’t think straight": [
    "To feel unable to think rationally due to overwhelming emotion."
  ],
  "I don’t buy it": [
    "I am not convinced; I doubt its truth."
  ],
  "Icing on the cake": [
    "Something that makes a good situation even better."
  ],
  "Ignorance is bliss": [
    "To remain unaware of things that could cause stress; sometimes it’s better not to know."
  ],
  "Ill at ease": [
    "To feel uncomfortable or worried in a situation."
  ],
  "In a jiffy": [
    "Very quickly; in a moment or two."
  ],
  "In a nutshell": [
    "Briefly and concisely; in a few words."
  ],
  "In a pickle": [
    "Experiencing a difficult situation; in trouble."
  ],
  "In a tight corner/spot": [
    "In a difficult or awkward situation."
  ],
  "In apple-pie order": [
    "In perfect order; neatly arranged."
  ],
  "In black and white": [
    "In writing; printed or recorded."
  ],
  "In cold blood": [
    "Angrily or cruelly, without any emotions; deliberately."
  ],
  "In deep water": [
    "In great difficulty; in trouble."
  ],
  "In dire straits": [
    "In a very bad or difficult situation."
  ],
  "In full swing": [
    "Very active; at the height of activity."
  ],
  "In high/good spirits": [
    "Full of hope and enthusiasm; joyful; cheerful."
  ],
  "In seventh heaven": [
    "Extremely happy; in delight."
  ],
  "In the air": [
    "When an emotion or idea is on everyone’s mind; prevalent."
  ],
  "In the blink of an eye": [
    "Within a very short period of time; almost instantly."
  ],
  "In the blues": [
    "Cheerless and depressed; low-spirited."
  ],
  "In the dark": [
    "To not know something others are aware of."
  ],
  "In the doldrums": [
    "In low spirits and despair."
  ],
  "In the driver's seat": [
    "In charge or in control of a situation."
  ],
  "In the eye of a storm": [
    "In the middle of a difficult situation."
  ],
  "In the fast lane": [
    "A life filled with great excitement."
  ],
  "In the good books": [
    "In favour with someone."
  ],
  "In the heat of the moment": [
    "Acting impulsively under strong emotions."
  ],
  "In the long run": [
    "Eventually after a significant time."
  ],
  "In the nick of time": [
    "At the very last possible moment."
  ],
  "In the pink": [
    "In good health."
  ],
  "In the same boat": [
    "Facing the same difficult situation."
  ],
  "In the soup": [
    "In trouble or difficulty."
  ],
  "In the teeth of": [
    "In spite of opposition or difficulty."
  ],
  "In vogue": [
    "Popular or in fashion."
  ],
  "Ins and outs": [
    "Full details or complexities of something."
  ],
  "It’s Greek to me": [
    "I cannot understand it at all."
  ],
  "It’s Raining Cats and Dogs": [
    "It’s raining very heavily."
  ],
  "Ivory towers": [
    "Detachment and seclusion from practical affairs."
  ],
  "Jump the gun": [
    "Start something too soon or prematurely."
  ],
  "Keep a straight face": [
    "To maintain a serious expression despite wanting to laugh."
  ],
  "Keep an ear to the ground": [
    "Stay informed about developments."
  ],
  "Keep at arm’s length": [
    "Maintain a safe or distant relationship."
  ],
  "Keep in touch": [
    "Continue to communicate with someone."
  ],
  "Keep one’s head": [
    "Remain calm and composed in difficult situations."
  ],
  "Keep under one’s hat": [
    "Keep something secret or confidential."
  ],
  "Keep up appearances": [
    "To pretend to be happier or richer so as to conceal the real situation."
  ],
  "Keep your chin up": [
    "To remain cheerful and hopeful in difficult circumstances."
  ],
  "Keep/hold something at bay": [
    "To control something and prevent it from causing you problems or moving closer."
  ],
  "Kick the bucket": [
    "To die."
  ],
  "Kicked up a row": [
    "To make a great fuss or cause a disturbance."
  ],
  "Kill two birds with one stone": [
    "To achieve two results with a single effort."
  ],
  "Kith and kin": [
    "One’s blood relatives or family members."
  ],
  "Know something inside out": [
    "To know everything about something thoroughly."
  ],
  "Latin and Greek": [
    "Unable to understand."
  ],
  "Lay out": [
    "Spend."
  ],
  "Lead someone by the nose": [
    "To completely control or dominate someone."
  ],
  "Learn by heart": [
    "To memorize something."
  ],
  "Learn/Know the ropes": [
    "To learn how to do a job or task properly."
  ],
  "Leave no stone unturned": [
    "To try every possible course of action in order to achieve something."
  ],
  "Leaves you in the lurch": [
    "To desert someone in difficulties."
  ],
  "Left out in cold": [
    "To be ignored."
  ],
  "Lend me your ear": [
    "Pay attention to me."
  ],
  "Lend someone a hand": [
    "To help or assist, especially voluntarily."
  ],
  "Let bygones be bygones": [
    "To forgive and forget past conflicts."
  ],
  "Let sleeping dogs lie": [
    "To avoid old controversies and let things remain undisturbed."
  ],
  "Let the cat out of the bag": [
    "To reveal a secret carelessly or by mistake."
  ],
  "Let the chips fall where they may": [
    "To accept whatever happens without worrying about the consequences."
  ],
  "Let the grass grow under one’s feet": [
    "To remain idle and do nothing."
  ],
  "Let your hair down": [
    "To behave freely and uninhibitedly / to relax and enjoy."
  ],
  "Level playing field": [
    "A situation where everyone has a fair and equal chance to succeed."
  ],
  "Light at the end of the tunnel": [
    "Signs of improvement in a difficult situation."
  ],
  "Like a shag on a rock": [
    "Completely alone."
  ],
  "Like two peas in a pod": [
    "Things that are very similar in appearance or always together."
  ],
  "Lily-livered": [
    "Not brave or cowardly."
  ],
  "Lion’s mouth": [
    "A difficult or dangerous situation."
  ],
  "Live from hand to mouth": [
    "To survive with just enough money, without saving anything extra."
  ],
  "Lock, stock and barrel": [
    "Completely; including all or every part of something."
  ],
  "Look before you leap": [
    "Think carefully about the consequences before acting."
  ],
  "Look down your nose at": [
    "Regard with contempt or consider someone inferior."
  ],
  "Loosen the purse strings": [
    "To increase the money available for expenditure."
  ],
  "Lose face": [
    "To become embarrassed or lose respect."
  ],
  "Lose one’s head": [
    "To panic or lose self-control."
  ],
  "Lose your marbles": [
    "To become mentally confused or insane."
  ],
  "Made a clean breast of": [
    "To admit or confess something fully."
  ],
  "Made light of": [
    "To treat something lightly or with little importance."
  ],
  "Maiden speech": [
    "The first speech ever given by someone."
  ],
  "Make a beeline for": [
    "To go straight to something."
  ],
  "Make a hash of": [
    "To do something very badly or make a mess of it."
  ],
  "Make a quick buck": [
    "To earn money quickly and easily."
  ],
  "Make head or tail of something": [
    "To understand or figure something out."
  ],
  "Make no bones about": [
    "To state something clearly and without hesitation."
  ],
  "Make one’s blood boil": [
    "To become extremely angry."
  ],
  "Make one’s mark": [
    "To distinguish oneself or attain recognition."
  ],
  "Make up with (someone)": [
    "To settle differences and become friendly again."
  ],
  "Making hay while the sun shines": [
    "To take advantage of a favorable opportunity."
  ],
  "Mealy mouthed": [
    "To be afraid to state something directly or to speak insincerely."
  ],
  "Method to my madness": [
    "A reason or purpose behind apparently crazy or random actions."
  ],
  "Milk and water": [
    "Weak ideas or statements."
  ],
  "Much ado about nothing": [
    "Making a big fuss over a small matter."
  ],
  "Neck of the woods": [
    "Neighbourhood or region."
  ],
  "New kid on the block": [
    "Someone new to a place or activity."
  ],
  "Nine days’ wonder": [
    "A short-lived sensation."
  ],
  "Nip in the bud": [
    "To stop something at the start before it develops."
  ],
  "No love lost between": [
    "There is intense dislike or people are not on good terms."
  ],
  "Not fit to hold a candle": [
    "Inferior to or cannot be compared to another."
  ],
  "Not hold water": [
    "To not seem reasonable or believable."
  ],
  "Not mince words": [
    "To be blunt or frank."
  ],
  "Not to look a gift horse in the mouth": [
    "To not find fault with what is received as a gift."
  ],
  "Off and on / On and Off": [
    "Occasionally or periodically."
  ],
  "It’s a small world": [
    "People often meet unexpectedly or have common acquaintances."
  ],
  "Lock horns": [
    "To get into an argument or fight."
  ],
  "Make one's flesh crawl/creep": [
    "To be very frightened or disgusted."
  ],
  "Mouth watering": [
    "Appealing to taste; looks or smells delicious."
  ],
  "Move heaven and earth": [
    "Do everything possible to achieve something."
  ],
  "Not one’s cup of tea": [
    "Not something one likes or enjoys."
  ],
  "Null and void": [
    "Invalid; without legal force."
  ],
  "Of the first water": [
    "Of the best quality."
  ],
  "Off the hook": [
    "No longer in difficulty or trouble."
  ],
  "On a roll": [
    "To be experiencing a period of repeated success."
  ],
  "On cloud nine": [
    "Extremely happy and excited."
  ],
  "On tenterhooks": [
    "In suspense or anxious."
  ],
  "On the back burner": [
    "To temporarily not deal with something as it is less urgent."
  ],
  "On the ball": [
    "To be alert and quick to respond."
  ],
  "On the breadline": [
    "Very poor or living at a subsistence level."
  ],
  "On the brink/verge of": [
    "At the edge of a major change or event."
  ],
  "On the cards": [
    "Likely to happen or probable."
  ],
  "On the face of it": [
    "According to what appears on the surface."
  ],
  "On the horizon": [
    "An event that is likely to happen soon."
  ],
  "On the same page": [
    "To be in agreement or think in the same way."
  ],
  "On the spur of the moment": [
    "Acting impulsively without thinking."
  ],
  "On the wane": [
    "On the decline or decreasing."
  ],
  "On thin ice": [
    "In a dangerous or risky situation."
  ],
  "Once and for all": [
    "To bring to an end conclusively or finally."
  ],
  "Once bitten, twice shy": [
    "An unpleasant experience makes one cautious for future."
  ],
  "Once in a blue moon": [
    "Rarely or very infrequently."
  ],
  "Out of date": [
    "Out of date."
  ],
  "Out of sorts": [
    "To be unwell or slightly sick."
  ],
  "Out of the blue": [
    "Completely unexpectedly."
  ],
  "Out of the question": [
    "Impossible."
  ],
  "Out of the woods": [
    "Out of the woods."
  ],
  "Over the moon": [
    "Extremely happy or delighted."
  ],
  "Pandora’s Box": [
    "A source of many unforeseen problems or trouble."
  ],
  "Part and parcel": [
    "An essential or integral element."
  ],
  "Pass the buck": [
    "To refuse responsibility or blame someone else."
  ],
  "Pass the hat round/around": [
    "To collect money."
  ],
  "Pat on the back": [
    "To praise or approve for doing something good."
  ],
  "Pay lip service": [
    "To pretend to agree or say something without meaning it."
  ],
  "Penny wise and pound foolish": [
    "Careful with trivial matters but wasteful in large issues."
  ],
  "Pig in a poke": [
    "Something bought without examining properly."
  ],
  "Pillar to post": [
    "Moving from one place to another repeatedly."
  ],
  "Pipe dream": [
    "A dream or idea that is unlikely to happen."
  ],
  "Play devil’s advocate": [
    "To argue the opposite just for the sake of argument."
  ],
  "Play it by ear": [
    "To do something without special preparation or to improvise."
  ],
  "Play one’s ace": [
    "To use one’s best weapon or resource."
  ],
  "Play to the gallery": [
    "To seek to win approval or to impress others."
  ],
  "Play with fire": [
    "To do something dangerous or take a foolish risk."
  ],
  "Played ducks and drakes": [
    "To squander or waste recklessly."
  ],
  "Pocket an insult": [
    "To bear an insult quietly or tolerate it without protest."
  ],
  "Point-blank": [
    "Directly or very close."
  ],
  "Poke one’s nose": [
    "To interfere or meddle in others’ affairs."
  ],
  "Pour/Throw cold water": [
    "To discourage by showing indifference."
  ],
  "Pull someone up": [
    "To criticize or reprimand someone."
  ],
  "Pull someone’s leg": [
    "To play a joke on or tease someone."
  ],
  "Pull strings": [
    "To use personal influence."
  ],
  "Pull the plug": [
    "To stop something from happening or continuing."
  ],
  "Pull up your socks": [
    "To put in extra effort or improve performance."
  ],
  "Pull yourself together": [
    "To calm yourself down and behave appropriately."
  ],
  "Pulled all the stops": [
    "To do something with maximum effort or ability."
  ],
  "Put off": [
    "To postpone or delay something."
  ],
  "Put one’s foot down": [
    "To take a firm stand or assert authority."
  ],
  "Put two and two together": [
    "To deduce or reason logically from facts."
  ],
  "Putting the cart before the horse": [
    "To do things in the wrong order."
  ],
  "Queer pitch": [
    "To spoil somebody’s chance of doing something."
  ],
  "Rained on the bride’s parade": [
    "To spoil and ruin someone’s happiness or plans."
  ],
  "Raise a few eyebrows": [
    "To cause surprise or mild shock in others."
  ],
  "Raise the alarm": [
    "To warn of a dangerous situation."
  ],
  "Ran in the groove": [
    "To move in harmony or smoothly."
  ],
  "Rat race": [
    "Fierce competition for power or success."
  ],
  "Read between the lines": [
    "To find a hidden meaning not explicitly stated."
  ],
  "Red-tape": [
    "Official procedures causing delay or excessive bureaucracy."
  ],
  "Rest on one’s laurels": [
    "To be satisfied with past success and not make further effort."
  ],
  "Ring a bell": [
    "To sound familiar or remind you of something."
  ],
  "Rise like a phoenix": [
    "To become successful again or to emerge with new life."
  ],
  "Rise to the occasion": [
    "To deal successfully with a difficult situation."
  ],
  "Rock the boat": [
    "To disturb a stable situation."
  ],
  "Roll up your sleeves": [
    "To get ready to do something difficult or hard work."
  ],
  "Rub somebody the wrong way": [
    "To irritate or annoy someone."
  ],
  "Run out of steam": [
    "To lose impetus or enthusiasm and stop doing something."
  ],
  "Rule the roost": [
    "To dominate or make all the decisions; be in complete control."
  ],
  "Salt of the earth": [
    "A good, reliable, honest person."
  ],
  "Scapegoats": [
    "People who are blamed or punished for others’ misdeeds."
  ],
  "Scrape the bottom of the barrel": [
    "To use one’s last and weakest resource."
  ],
  "See eye to eye": [
    "To be in full agreement with someone."
  ],
  "See the light of day": [
    "To become publicly known or visible."
  ],
  "Selling like hot cakes": [
    "Selling very quickly and in large numbers."
  ],
  "Separate the wheat from the chaff": [
    "To sort out the valuable from the worthless."
  ],
  "Shake off": [
    "To get rid of something."
  ],
  "Sharp as a tack": [
    "Extremely intelligent and mentally active."
  ],
  "Shed crocodile tears": [
    "To pretend to be sad or show false sympathy."
  ],
  "Shot in the dark": [
    "A random attempt with little chance of success."
  ],
  "Sit on the fence": [
    "To remain neutral or undecided between two options."
  ],
  "Snake in the grass": [
    "An unreliable and deceitful person."
  ],
  "Snowed under": [
    "Busy."
  ],
  "Soft option": [
    "Easy and agreeable option."
  ],
  "Sought after": [
    "In great demand."
  ],
  "Sow wild oats": [
    "To waste time by doing foolish things, especially in youth."
  ],
  "Speak of the devil": [
    "The person we were just talking about showed up."
  ],
  "Speaks volumes": [
    "Gives enough proof without using words."
  ],
  "Spick and span": [
    "Very neat, clean, or tidy."
  ],
  "Spill the beans": [
    "Disclose the secrets accidentally."
  ],
  "Spin one’s wheels": [
    "Expel much effort for little or no gain."
  ],
  "Split one’s sides (laughing)": [
    "Be extremely amused."
  ],
  "Spread like wildfire": [
    "Spread rapidly."
  ],
  "Slap on the wrist": [
    "Mild punishment."
  ],
  "Sleep on it": [
    "Delay making a decision until the next day."
  ],
  "Square peg in a round hole": [
    "A misfit in the environment."
  ],
  "Stab someone in the back": [
    "Betray someone."
  ],
  "Stand by": [
    "To support or remain loyal to someone."
  ],
  "Steal someone’s thunder": [
    "Take credit for something someone else did."
  ],
  "Start/set/get the ball rolling": [
    "To start doing something."
  ],
  "Stick to one’s guns": [
    "Maintain one’s own opinion; not change one’s decision despite opposition."
  ],
  "Steer clear of": [
    "Avoid someone or something because it is dangerous for you."
  ],
  "Still waters run deep": [
    "Have passion or great intelligence underneath a calm expression."
  ],
  "Stir up a hornet’s nest": [
    "Cause anger in many people or raise controversy."
  ],
  "Straight from the horse’s mouth": [
    "Receive information directly from the person involved."
  ],
  "Strain every nerve": [
    "Work very hard."
  ],
  "Strike while the iron is hot": [
    "To act at the right time or grab a favourable opportunity promptly."
  ],
  "Struck several bad patches": [
    "Had many professional difficulties."
  ],
  "Suit you to a T": [
    "To be ideal or perfectly appropriate for one."
  ],
  "Sweep under the carpet": [
    "To hide a problem or try to keep it secret instead of dealing with it."
  ],
  "Swollen-headed": [
    "Pride."
  ],
  "Sword of Damocles": [
    "Imminent danger."
  ],
  "Take a cue from someone": [
    "Learn and act by being strongly influenced by someone."
  ],
  "Take exception to": [
    "To object strongly."
  ],
  "Take heart": [
    "To take courage or to gain confidence."
  ],
  "Take to one’s heels": [
    "To run away or flee in fear."
  ],
  "Take with a pinch/grain of salt": [
    "Not believe completely something that you are told."
  ],
  "Take the bull by the horn": [
    "To face a difficult or dangerous situation in a very direct or confident way."
  ],
  "Takes after": [
    "To be similar in appearance."
  ],
  "Taking a toll on": [
    "To harm or damage someone or something, especially in a gradual way."
  ],
  "Talked over": [
    "Discussed."
  ],
  "Talking through her hat": [
    "Talking nonsense."
  ],
  "The bad egg": [
    "A dishonest or ill-behaved person."
  ],
  "The early bird catches the worm": [
    "One who arrives first gets the best chance at success."
  ],
  "The elephant in the room": [
    "A big problem everyone is ignoring or afraid to talk about."
  ],
  "The grass is greener on the other side": [
    "Other people always seem to be in a better situation, although it might not be true."
  ],
  "Teething problems": [
    "Problems at the start of a new project."
  ],
  "The green-eyed monster": [
    "Jealousy."
  ],
  "The last straw": [
    "Final problem in a series of difficulties that makes a situation unbearable."
  ],
  "The Lion’s share": [
    "The biggest and best part of a whole."
  ],
  "The man in the street": [
    "The ordinary man."
  ],
  "The pot calling the kettle black": [
    "People are guilty of the very fault they identify in others."
  ],
  "The pros and cons": [
    "For and against; advantages and disadvantages."
  ],
  "The seamy side": [
    "The unpleasant aspects."
  ],
  "The thin end of the wedge": [
    "Start of harmful development; beginning of something bad."
  ],
  "The whys and wherefores": [
    "Underlying reasons or causes of something."
  ],
  "Thick as thieves": [
    "Having a close friendship."
  ],
  "Threw a spanner": [
    "Do something that prevents a plan or activity from succeeding."
  ],
  "Through thick and thin": [
    "Support under all circumstances."
  ],
  "Throw caution to the wind": [
    "Behave recklessly without worrying about the risk."
  ],
  "Throw in the towel": [
    "Acknowledge defeat or surrender."
  ],
  "Tickled pink": [
    "Very pleased."
  ],
  "Tie the knot": [
    "Get married."
  ],
  "To accept the gauntlet": [
    "To accept or respond to a challenge."
  ],
  "To air dirty linen in public": [
    "To discuss private affairs in public."
  ],
  "To be devil’s advocate": [
    "To raise a counter argument just for the sake of it."
  ],
  "To be fair and square": [
    "To be honest; according to the rules."
  ],
  "To be in a fix": [
    "To be in a difficult situation."
  ],
  "To be on pins and needles": [
    "To be in an agitated state of suspense."
  ],
  "To be on the horns of a dilemma": [
    "To be in a difficult situation or choice."
  ],
  "To be taken aback": [
    "To be surprised or shocked."
  ],
  "To beat a retreat": [
    "To run away in fear; to withdraw."
  ],
  "To beat the clock": [
    "To perform a task within the time limit."
  ],
  "To blow hot and cold": [
    "To be friendly and unfriendly at the same time; vacillating."
  ],
  "To bring to light": [
    "To reveal clearly."
  ],
  "To burn one’s fingers": [
    "To suffer unpleasant consequences as a result of one's actions."
  ],
  "To burn the candle at both ends": [
    "To work excessively hard or keep busy all the time."
  ],
  "To call a spade a spade": [
    "To be frank or say the truth about something, even if it is not polite."
  ],
  "To clip one’s wings": [
    "To restrict someone’s freedom."
  ],
  "To come out in the open": [
    "To become public or evident."
  ],
  "To cry wolf": [
    "To raise a false alarm or ask for help when you do not need it."
  ],
  "To cudgel one’s brains": [
    "To think hard."
  ],
  "To cut a sorry figure": [
    "Created a wrong impression."
  ],
  "To eat humble pie": [
    "To accept defeat or suffer humiliation."
  ],
  "Throw up the sponge": [
    "To surrender; to acknowledge defeat."
  ],
  "Till the cows come home": [
    "For a very long time."
  ],
  "Tit for tat": [
    "To do harm as done to you; counter attack."
  ],
  "To cut one's coat according to one's cloth": [
    "To live within one's means."
  ],
  "To die in harness": [
    "To continue occupation till death."
  ],
  "To draw the long bow": [
    "To exaggerate."
  ],
  "To end in smoke": [
    "To come to nothing; end without any practical result."
  ],
  "To feel at home": [
    "To feel easy and comfortable."
  ],
  "To fight tooth and nail": [
    "To make every possible effort; to fight furiously and fiercely."
  ],
  "To fish in troubled waters": [
    "To profit out of disturbance; to get benefit in bad situation."
  ],
  "To flog/beating a dead horse": [
    "To attempt the impossible; waste energy on an unalterable situation."
  ],
  "To foam at one’s mouth": [
    "To get very angry; to be enraged and shout."
  ],
  "To get away with": [
    "To escape from something."
  ],
  "To get cold feet": [
    "To experience nervousness or anxiety before one attempts to do something."
  ],
  "To gird up the loins": [
    "To prepare for hard work or a difficult situation."
  ],
  "To give the devil his due": [
    "To give encouragement or credit to an enemy; to give credit to a notorious person."
  ],
  "To go bananas": [
    "To become very excited or angry."
  ],
  "To go scot-free": [
    "To escape without punishment; unpunished."
  ],
  "To go the whole hog": [
    "To do something as completely as possible."
  ],
  "To go/run around in circles": [
    "To waste one’s time and energy doing trivial things; to keep doing something without achieving much."
  ],
  "To hail from": [
    "To come from a particular place."
  ],
  "To have a gut feeling": [
    "Strong instinct or intuition."
  ],
  "To have second thoughts": [
    "To reconsider."
  ],
  "To have something up one’s sleeve": [
    "To have a secret plan; have an alternative plan."
  ],
  "To have a sigh of relief": [
    "To suddenly feel very happy because something unpleasant has not happened or has ended."
  ],
  "To hit below the belt": [
    "To attack in an unfair manner; contrary to the principles of fairness."
  ],
  "To hammer out": [
    "To reach an agreement after long discussion."
  ],
  "To his heart's content": [
    "As much as one wants."
  ],
  "To judge a book by its cover": [
    "To evaluate people’s worth by their outward appearance."
  ],
  "To jump on the bandwagon": [
    "To follow popular trends; to get involved in an activity because it is likely to succeed."
  ],
  "To keep an eye on": [
    "To watch someone or something carefully; to be cautious."
  ],
  "To keep one’s temper": [
    "To remain calm."
  ],
  "To let someone off": [
    "To release someone from blame."
  ],
  "To lose ground": [
    "Becoming less acceptable."
  ],
  "To make a mountain out of a molehill": [
    "To give great importance to little things; exaggerate a minor problem."
  ],
  "To make amends": [
    "To compensate; to correct a mistake."
  ],
  "To keep the wolf away from the door": [
    "To keep away extreme poverty; to earn just enough for a living."
  ],
  "To keep under wraps": [
    "To keep secret."
  ],
  "To hit the sack": [
    "To prepare for sleep; to go to bed."
  ],
  "To make both ends meet": [
    "To live within one’s income; manage expenses with just enough funds."
  ],
  "To make up one’s mind": [
    "To decide what to do; decide firmly."
  ],
  "To meet one’s Waterloo": [
    "To experience defeat; to be defeated by someone who is too strong for you."
  ],
  "To miss the boat": [
    "To miss an opportunity; lose an opportunity."
  ],
  "To paddle one’s own canoe": [
    "Manage independently; to work independently."
  ],
  "To pay through the nose": [
    "To pay an extremely high price."
  ],
  "To pick holes in": [
    "To criticize someone; finding fault with."
  ],
  "To play fast and loose": [
    "To act in an unreliable way; to be playful."
  ],
  "To play second fiddle": [
    "Position has lesser importance than anybody else; take a subordinate role."
  ],
  "To pour oil on troubled water": [
    "To calm a dispute."
  ],
  "To put up with someone": [
    "Tolerate."
  ],
  "To raise a dust": [
    "To cause disruption or confusion."
  ],
  "To set the Thames on fire": [
    "To do a heroic deed; do wonderful or exciting things."
  ],
  "To show a clean pair of heels": [
    "To escape; ran away."
  ],
  "To smell a rat": [
    "Suspect a trick or deceit; detect something wrong."
  ],
  "To prime the pump": [
    "Encourage the growth or action of something."
  ],
  "To put a spoke in one’s wheel": [
    "To put a difficulty in the way of progress; thwart in the execution of the plan."
  ],
  "To speak one’s mind": [
    "To express one’s thoughts; to voice one’s thoughts plainly."
  ],
  "To stand on one’s feet": [
    "To be strong and independent."
  ],
  "To stand one’s ground": [
    "Refused to yield; refuse to change your opinion."
  ],
  "To stick one’s neck out": [
    "To take a risk."
  ],
  "To take a back seat": [
    "To become less important or to give up control over things."
  ],
  "To take a stock of": [
    "To assess and evaluate before taking a decision; to think carefully."
  ],
  "To take French leave": [
    "Absenting oneself without permission; leave without any intimation."
  ],
  "To take pains": [
    "To make efforts; try hard."
  ],
  "To take to heart": [
    "To be greatly affected by; to consider something very seriously."
  ],
  "To take to task": [
    "To be punished; to be rebuked or scolded."
  ],
  "To throw dust in one’s eyes": [
    "To deceive; to mislead or confuse."
  ],
  "To toe the line": [
    "To follow the lead; follow the rules strictly."
  ],
  "To turn a deaf ear": [
    "Disregard; refuse to obey; to be indifferent; neglect."
  ],
  "To turn over a new leaf": [
    "To change one’s behaviour for better; to begin again."
  ],
  "To win laurels": [
    "To achieve honours and glory."
  ],
  "Too many irons in the fire": [
    "Engaged in too many enterprises at the same time."
  ],
  "Took a leap in the dark": [
    "Took a risk; to do something without being certain of the outcome and result."
  ],
  "Tricks of the trade": [
    "Special skills or knowledge."
  ],
  "True colours": [
    "Real character; personality."
  ],
  "To take for granted": [
    "To assume something without question."
  ],
  "To take into account": [
    "To consider; to keep in mind."
  ],
  "To take one’s hat off (to someone)": [
    "To admire or respect."
  ],
  "To the manner born": [
    "Naturally suited for something."
  ],
  "To wrangle over an ass’s shadow": [
    "To fight over trifles."
  ],
  "Toffee-nosed": [
    "Snobbish; arrogant."
  ],
  "Took exception (to)": [
    "Objected; felt offended."
  ],
  "Took to their heels": [
    "Ran away."
  ],
  "Turn a blind eye": [
    "To ignore a situation, facts, or reality."
  ],
  "Turn up one’s nose": [
    "Treat other people with contempt; despise."
  ],
  "Twist someone’s arm": [
    "Force someone to do something by making it hard for them to refuse; persuade someone."
  ],
  "Two heads are better than one": [
    "It’s helpful to have the advice/opinion of a second person; two people working together can achieve more than a person working alone."
  ],
  "Under a cloud": [
    "Under suspicion."
  ],
  "Under duress": [
    "Under pressure; compulsion."
  ],
  "Under his nose": [
    "Right in front of someone, often without them noticing."
  ],
  "Under the weather": [
    "To not feel well; to feel sick or unhealthy; to be in low spirits"
  ],
  "Up a blind alley": [
    "Following a course of action that is certain to lead to an undesirable outcome."
  ],
  "Up in arms": [
    "To be angry; protesting vigorously about something; in rebellion."
  ],
  "Up to the mark": [
    "As good as the others; up to the required standard."
  ],
  "Upset someone’s applecart": [
    "To cause trouble, especially by spoiling someone’s plans."
  ],
  "Vanish/disappear into thin air": [
    "Disappear suddenly."
  ],
  "Vote with your feet": [
    "Show their disapproval; to show that you do not support something."
  ],
  "Walk the tightrope": [
    "Be very cautious; to be in a precarious situation requiring caution and skill."
  ],
  "Walking on thin ice": [
    "Doing something risky."
  ],
  "Water under the bridge": [
    "Something that can’t be changed anymore; something happened in the past and is no longer important or worth arguing about."
  ],
  "Weal and woe": [
    "Good times and bad times; joys and sorrows; in prosperity and adversity."
  ],
  "Wear and tear": [
    "Damage."
  ],
  "Wears his heart on his sleeve": [
    "Expresses his feelings openly; to show your true emotions."
  ],
  "Weather the storm": [
    "Survive a period of difficulty."
  ],
  "When it rains, it pours": [
    "Problems seem to happen together."
  ],
  "When pigs fly": [
    "Something that is impossible."
  ],
  "When the crunch comes": [
    "A critical moment near the end when a decisive action is needed."
  ],
  "Where there’s a will, there’s a way": [
    "If you have a strong determination to do something, then you can find a method to do it."
  ],
  "Whistle in the dark": [
    "Pretend to be unafraid; try to keep up his confidence."
  ],
  "White elephant": [
    "Costly and troublesome possession useless to its owner."
  ],
  "Whole nine yards": [
    "The entirety of something; everything all the way."
  ],
  "Wild goose chase": [
    "A worthless hunt or chase; futile search; unprofitable adventure."
  ],
  "Will-o-the-wisp": [
    "Something that is impossible to get or achieve; unreal imagining."
  ],
  "Went to the winds": [
    "Dissipated."
  ],
  "With open arms": [
    "Warmly welcome."
  ],
  "Word of mouth": [
    "Through the verbal sharing of information."
  ],
  "Worth its weight in gold": [
    "Very useful, valuable, or important."
  ],
  "Yeoman service": [
    "Excellent service; useful help in need."
  ],
  "Your guess is as good as mine": [
    "Have no idea of the answer."
  ],
  "Zero tolerance": [
    "A policy of not allowing any violations of a rule or law."
  ],
  "Zip your lip": [
    "Keep quiet about something."
  ],
  "Turn down": [
    "To reject or refuse."
  ],
  "Turn turtle": [
    "To overturn or capsize."
  ],
  "Wash one’s hands off something": [
    "To withdraw from responsibility; disclaim connection with."
  ]
}
{
  'A bird in the hand is worth two in the bush': [
    'Having something certain is better than the possibility of getting something better.'
  ],
  'A bird"s eye view': [ 'A general view from above.' ],
  'A blessing/boon in disguise': [ 'An apparent misfortune that eventually has good results.' ],
  'A blue-eyed boy': [ 'One who is favourite.' ],
  'A bolt from the blue': [ 'Something unexpected and unpleasant.' ],
  'A bone of contention': [ 'A cause of dispute or quarrel.' ],
  'A bull in a China shop': [ 'A clumsy person in a delicate situation.' ],
  'A cakewalk': [ 'An easy achievement or victory.' ],
  'A carrot and stick approach': [ 'Rewards and punishments that influence someone’s behaviour.' ],
  'A change of heart': [ 'A change in one’s opinion or feelings.' ],
  'A close-fisted person': [ 'A miser.' ],
  'A cold fish': [
    'Someone who seems unfriendly and who does not share his feelings.'
  ],
  'A cut above something': [ 'Superior to.' ],
  'A damp squib': [
    'A disappointing result or situation less impressive than expected.'
  ],
  'A dark horse': [ 'An unexpected winner or competitor of unknown capabilities.' ],
  'A dime a dozen': [ 'Very common and easily obtainable.' ],
  'A dog’s life': [ 'A miserable existence.' ],
  'A drop in a bucket': [ 'A very small part too insignificant to matter.' ],
  'A dry run': [ 'A rehearsal or practice session.' ],
  'A fire in someone’s belly': [ 'One who is energetic and enthusiastic about something.' ],
  'A fish out of water': [ 'A person in an unfamiliar or uncomfortable environment.' ],
  'A flying visit': [ 'A very short visit.' ],
  'A fool’s paradise': [ 'A state of happiness based on ignorance of potential trouble.' ],
  'A gentleman at large': [ 'A man without a job.' ],
  'A golden mean': [
    'Middle course between two extremes; neither too much nor too little.'
  ],
  'A green horn': [ 'An inexperienced man.' ],
  'A grey area': [ 'An unclear or undefined situation.' ],
  'A hairbreadth escape': [ 'A narrow escape.' ],
  'A hard nut to crack': [ 'A tough challenge or difficult person.' ],
  'A hornet’s nest': [ 'An unpleasant, difficult, or troublesome situation.' ],
  'A hot potato': [ 'A controversial or difficult issue.' ],
  'A house of cards': [ 'A fragile or unstable situation that can easily collapse.' ],
  'A kick in the teeth': [ 'A grave setback or great disappointment.' ],
  'A lame excuse': [ 'A weak or unsatisfactory explanation.' ],
  'A laughing stock': [ 'An object of ridicule or laughter.' ],
  'A left handed compliment': [ 'An ambiguous compliment that may be insulting.' ],
  'A leopard can’t change its spots': [ 'It is impossible for one to change one’s character.' ],
  'A little bird told me': [ 'To receive information from a secret source without naming it.' ],
  'A live wire': [ 'A person who is full of energy.' ],
  'A lot on your plate': [ 'Having many responsibilities or problems to deal with.' ],
  'A man of letters': [ 'A scholar; someone proficient in literary art.' ],
  'A man of straw': [ 'A man of no substance; a weak or cowardly person.' ],
  'A mare’s nest': [ 'A complicated situation or false invention.' ],
  'A needle in a haystack': [ 'Something very difficult to locate or attempt.' ],
  'A pain in the neck': [ 'Something or someone that is annoying or a nuisance.' ],
  'A Penelope’s web': [ 'An endless, never-ending job.' ],
  'A penny for your thoughts': [ 'A way of asking what someone is thinking.' ],
  'A picture paints a thousand words': [ 'An image conveying meaning more effectively than description.' ],
  'A piece of cake': [ 'A very easy task.' ],
  'A plum job': [ 'An easy, pleasant job that pays well.' ],
  'A queer fish': [ 'An eccentric or unconventional person.' ],
  'A red letter day': [ 'An important or memorable day.' ],
  'A red rag to a bull': [ 'An act certain to provoke someone.' ],
  'A rolling stone gathers no moss': [
    'A person who does not settle in one place and therefore gains no advantage.'
  ],
  'A rotten apple': [ 'A single bad person in a group.' ],
  'A safe pair of hands': [
    'A reliable person who can be trusted to do something efficiently.'
  ],
  'A sea change': [ 'A profound or notable transformation.' ],
  'A shot in the arm': [ 'Something that gives encouragement.' ],
  'A skeleton in the cupboard': [ 'An embarrassing fact or shameful secret to be kept hidden.' ],
  'A square deal': [ 'A fair and honest agreement.' ],
  'A stitch in time saves nine': [ 'Fixing a problem promptly prevents it from worsening.' ],
  'A stone’s throw away': [ 'A very short distance.' ],
  'A storm in a teacup': [ 'A big fuss or excitement about a trivial matter.' ],
  'A thorn in the flesh': [ 'A source of continual annoyance or trouble.' ],
  'A turning point': [ 'A time when an important change begins.' ],
  'A wet blanket': [ 'A person who discourages enjoyment or enthusiasm.' ],
  'A wolf in sheep’s clothing': [ 'A dangerous person pretending to be harmless.' ],
  'Above board': [ 'Honest and frank; without any secret.' ],
  'Above/Over one’s head': [ 'Beyond one’s capability to understand something.' ],
  'Achilles’ heel': [ 'A weakness or vulnerable point.' ],
  'Acid test': [ 'Definitive proof of truth or falsehood.' ],
  'Actions speak louder than words': [
    'What you do is more important than what you say; intentions judged by actions.'
  ],
  'Add fuel to the fire/flames': [ 'Make a bad situation worse.' ],
  'Add insult to injury': [
    'To further a loss with mockery, making a bad situation even worse.'
  ],
  'After one’s own heart': [ 'Having likes and dislikes similar to one’s own.' ],
  'Against the clock': [ 'Work very fast to complete something within a deadline.' ],
  'Alive and kicking': [ 'In good health.' ],
  'All agog': [ 'Amazed or full of interest and excitement.' ],
  'All and sundry': [ 'Everybody without distinction; all included.' ],
  'All at sea': [ 'Puzzled; in a state of confusion or lost.' ],
  'All eyes': [ 'Watching eagerly; to watch something intently.' ],
  'All eyes and ears': [ 'To be attentive and fully focused on something.' ],
  'All moonshine': [ 'Nonsense; far from reality or concocted.' ],
  'All our might and main': [ 'Exercising full force; with all one’s strength and energy.' ],
  'All thumbs': [ 'Clumsy; physically awkward.' ],
  'Alpha and omega': [ 'The beginning and the end; everything.' ],
  'Alphabet soup': [ 'A confusing jumble of abbreviations or acronyms.' ],
  'An eye opener': [ 'A shocking revelation.' ],
  'An iron hand': [ 'Strict and harsh control.' ],
  'An iron will': [ 'A firm opinion; strong determination.' ],
  'An open book': [ 'Someone or something with no secrets; fully transparent.' ],
  'Apple of discord': [ 'The cause of a quarrel or animosity.' ],
  'Apple of one’s eye': [ 'Someone very precious or dearly loved.' ],
  'Apples and oranges': [ 'Unequal comparisons between two unlike things.' ],
  'Argus-eyed': [ 'Carefully observant and attentive; vigilant.' ],
  'Armed to the teeth': [ 'Heavily armed or fortified.' ],
  'Around the corner': [ 'Happening very soon; occurring shortly.' ],
  'As daft as a brush': [ 'Extremely silly or foolish.' ],
  'As fit as a fiddle': [ 'Strong, healthy, in top condition.' ],
  'As hard as a nail': [ 'Emotionless or unrelenting; having no feelings.' ],
  'As the crow flies': [ 'By the shortest, direct route in a straight line.' ],
  'At a crossroads': [
    'A point in life where decisions will have long-term consequences.'
  ],
  'At a snail’s pace': [ 'Doing something very slowly.' ],
  'At beck and call': [ 'Always available to help; at one’s disposal.' ],
  'At cross purposes': [
    'Having opposing viewpoints or intentions; misunderstanding each other.'
  ],
  'At daggers drawn': [ 'To be bitterly hostile or open enemies.' ],
  'At large': [ 'A criminal who has escaped or is not yet captured.' ],
  'At loggerheads': [ 'In conflict with someone; to disagree strongly.' ],
  'At loose ends': [ 'In an uncertain or unsettled situation.' ],
  'At one’s wits’ end': [ 'Completely confused or perplexed.' ],
  'At sixes and sevens': [ 'In disorder or confusion.' ],
  'At the drop of a hat/dime': [ 'Without any hesitation; instantly or without planning.' ],
  'At the eleventh hour': [ 'At the very last moment; just before the deadline.' ],
  'Back out of': [ 'Withdraw from a commitment.' ],
  'Back to square one': [ 'Return to the starting point; having to start all over again.' ],
  'Back to the drawing board': [ 'An idea has failed and must be redesigned.' ],
  'Back up': [ 'Defend or support.' ],
  'Backseat driver': [
    'Interfering in affairs without authority; someone who offers unsolicited advice.'
  ],
  'Bad blood': [ 'Angry feeling or enmity between people.' ],
  'Bag and baggage': [ 'With all one’s belongings; with full luggage.' ],
  'Baker’s dozen': [ 'A group of 13 items; one more than a usual dozen.' ],
  'Ball is in your court': [
    'It is up to you to make the next decision or be responsible for further action.'
  ],
  'Barking up the wrong tree': [
    'Trying to do something in a way that will not work or accusing the wrong person.'
  ],
  'Be all ears': [ 'Listening intently; eager to hear.' ],
  'Be behind the times': [ 'Outdated or old-fashioned.' ],
  'Be glad to see the back of': [ 'Feel happy when someone or something leaves.' ],
  'Be going places': [ 'To be talented and likely to succeed.' ],
  'Be hard up': [ 'To be very short of money.' ],
  'Be in the red': [ 'To be in debt or losing money.' ],
  'Be in two minds': [ 'Unable to decide; holding conflicting opinions.' ],
  'Be like chalk and cheese': [ 'To be completely different from each other.' ],
  'Be out for the count': [ 'To be unconscious or in deep sleep.' ],
  'Be out of order': [ 'An object or device not working properly.' ],
  'Be under somebody’s thumb': [ 'To be completely controlled or dominated by someone.' ],
  'Be wet behind the ears': [ 'To be inexperienced or naive.' ],
  'Bear a grudge': [
    'To hold resentment or feel anger against someone for a past incident.'
  ],
  'Bear fruit': [ 'To yield positive results.' ],
  'Bear the brunt of': [ 'To suffer the worst of something; to endure the maximum impact.' ],
  'Bear the palm': [ 'Win or be declared the victor.' ],
  'Bear up with': [ 'Endure a difficult situation; be strong enough to continue.' ],
  'Beat about/around the bush': [ 'Speak vaguely or avoid the main topic.' ],
  'Bed of roses': [ 'A comfortable, pleasant situation or life.' ],
  'Behind closed doors': [ 'Do something secretly.' ],
  'Behind one’s back': [ 'In someone’s absence; without their knowledge.' ],
  'Behind the eight ball': [ 'In a difficult or disadvantaged position.' ],
  'Behind the scenes': [ 'Secretly or out of public view.' ],
  'Bell the cat': [ 'Do the impossible or most dangerous job.' ],
  'Below the belt': [ 'A cruel or unfair action.' ],
  'Bend over backwards': [ 'Try very hard to accommodate or please someone.' ],
  'Beside oneself': [ 'Almost out of one’s senses with emotion.' ],
  'Beside the mark': [ 'Irrelevant or not applicable.' ],
  'Best of both worlds': [ 'A situation offering two different advantages simultaneously.' ],
  'Best thing since sliced bread': [ 'A truly remarkable innovation or idea.' ],
  'Better late than never': [ 'It is better to arrive late than not to come at all.' ],
  'Between a rock and a hard place': [ 'Stuck between two very bad options.' ],
  'Between Scylla and Charybdis': [ 'Choice between two equally unpleasant alternatives.' ],
  'Between the devil and the deep blue sea': [ 'Stuck between two very bad options.' ],
  'Beyond the pale': [ 'Unacceptable or unreasonable.' ],
  'Bid defiance': [ 'To offer resistance; disregard recklessly.' ],
  'Birds of the same feather': [ 'Two people of the same character or interests.' ],
  'Bite off more than one can chew': [ 'Take on more responsibility than one can handle.' ],
  'Bite someone’s head off': [ 'Speak angrily without any reason.' ],
  'Bite the bullet': [
    'To force yourself to do something unpleasant because inevitable.'
  ],
  'Bite the dust': [ 'Suffer a defeat; die.' ],
  'Bite your tongue': [ 'Stop yourself from saying something.' ],
  'Black and blue': [ 'Describe someone badly bruised or to beat mercilessly.' ],
  'Black sheep': [ 'A single bad person in a group because of bad conduct.' ],
  'Blaze a trail': [ 'Lead the way as a pioneer; initiate something new.' ],
  'Blow one’s own trumpet': [ 'Praise oneself; talk boastfully about one’s achievements.' ],
  'Blue-blooded': [ 'Of noble birth.' ],
  'Body and soul': [ 'With all your energy.' ],
  'Boil the ocean': [ 'Undertaking an impossible chore or task.' ],
  'Bone to pick': [
    'Cause of quarrel; to be angry about something and want to discuss it.'
  ],
  'Born with a silver spoon in one’s mouth': [ 'To be born into a wealthy, privileged family.' ],
  'Bread and butter': [ 'The means of livelihood; main source of income.' ],
  'Break a leg': [ 'To wish someone good luck or to perform well.' ],
  'Break in': [ 'To force entry into a building illegally.' ],
  'Break new/fresh ground': [ 'To innovate; to do or discover something new.' ],
  'Break the bank': [
    'To be very expensive or to win more money than is held by the bank.'
  ],
  'Break the ice': [
    'To initiate a conversation or to break a painful silence and make someone comfortable.'
  ],
  'Breathing down someone’s neck': [ 'Watching all someone’s actions closely; monitoring them.' ],
  'Bring about': [ 'Cause to happen.' ],
  'Bring home the bacon': [ 'To be successful; to earn a living.' ],
  'Bring someone to book': [ 'To punish someone for wrongdoing or hold them accountable.' ],
  'Bring the house down': [ 'To make an audience applaud enthusiastically.' ],
  'Broke down': [ 'Wept bitterly; cried.' ],
  'Broken reed': [ 'A weak person; support that failed.' ],
  'Build castles in the air': [ 'To have unrealistic ideas or dreams.' ],
  'Bull’s-eye': [ 'The centre of a target; a perfect hit.' ],
  'Burn one’s bridges/boats': [ 'To destroy all relations or make return impossible.' ],
  'Burn the midnight oil': [ 'To work or study very late at night.' ],
  'Burning question': [ 'An important, pressing question or issue.' ],
  'Bury the hatchet': [ 'To make peace; end a quarrel.' ],
  'Butterflies in the stomach': [ 'To be anxious and nervous.' ],
  'By and by': [ 'Gradually; after a while.' ],
  'By and large': [ 'In general; on the whole.' ],
  'By courtesy of': [ 'Given or allowed by; with kindly consideration.' ],
  'By fair means or foul': [ 'In any way, by honest or dishonest methods.' ],
  'By fits and starts': [ 'Unsteadily; irregularly.' ],
  'By hook or by crook': [ 'By any means, good or bad; using whatever methods.' ],
  'By leaps and bounds': [ 'Very quickly; rapidly; swiftly.' ],
  'By the skin of one’s teeth': [ 'By the narrowest margin; barely manage to achieve something.' ],
  'Call in question': [ 'To challenge; dispute something.' ],
  'Call it a day': [ 'To decide to stop doing something and go home.' ],
  'Call on': [ 'To pay a visit.' ],
  'Call the shots': [ 'To be in control; to make decisions.' ],
  'Called for': [ 'To require something; to demand.' ],
  'Can’t cut the mustard': [ 'To be unable to do a job; not measure up.' ],
  'Carry out': [ 'To execute or complete something.' ],
  'Carry the day': [ 'To win a victory; emerge as the winner.' ],
  'Cat nap': [ 'To have disturbed sleep; a brief sleep.' ],
  'Catch 22': [ 'A particular situation in which one cannot do anything.' ],
  'Catch a tartar': [ 'To catch someone unexpectedly powerful or troublesome.' ],
  'Catch red-handed': [
    'To catch someone doing something illegal; in the act of committing a crime.'
  ],
  'Change hands': [ 'Pass from one person to another; change of ownership.' ],
  'Chapter and verse': [ 'To give exact information or minute details.' ],
  'Charley horse': [ 'A cramp in a muscle.' ],
  'Cheek by jowl': [ 'Very close together.' ],
  'Chew the cud': [ 'To think slowly and carefully about something.' ],
  'Chew the fat': [ 'Gossip and make small talk; have friendly talks.' ],
  'Chew the scenery': [ 'To act over-dramatically.' ],
  'Chicken out': [
    'To decide not to do something because you are too frightened; withdraw.'
  ],
  'Chicken-hearted': [ 'Cowardly; easily frightened.' ],
  'Child’s play': [ 'Something very easy to do; a very easy task.' ],
  'Chill out': [ 'To calm down.' ],
  'Chinks in the armour': [ 'Small flaws or weaknesses.' ],
  'Chip off the old block': [ 'Resembling one’s father in character or behaviour.' ],
  'Cloak and dagger': [ 'An activity involving secrecy and mystery.' ],
  'Close shave': [ 'A narrow escape from danger or disaster.' ],
  'Cock and bull story': [ 'An unbelievable or absurd story.' ],
  'Cold comfort': [ 'Slight satisfaction; little consolation.' ],
  'Come hell or high water': [ 'In spite of any obstacles; no matter what.' ],
  'Come in handy': [ 'To turn out to be useful.' ],
  'Come of age': [ 'To mature and develop fully.' ],
  'Come rain or shine': [ 'Under any circumstances; whatever the weather.' ],
  'Come to blows': [ 'To get into a physical fight.' ],
  'Come to light': [ 'To be revealed; become known publicly.' ],
  'Come what may': [ 'No matter what happens.' ],
  'Cook the books': [ 'To falsify financial records; dishonest accounting.' ],
  'Cool as a cucumber': [ 'Not nervous or emotional; calm and composed.' ],
  'Cool your heels': [ 'To be kept waiting; unwillingly wait for something or someone.' ],
  'Cost an arm and a leg': [ 'To be very expensive; a large amount of money.' ],
  'Couch potato': [ 'A person who watches too much television; a lazy person.' ],
  'Crack someone up': [ 'Laugh out loud; to make someone laugh.' ],
  'Cross one’s mind': [ 'To think of something; to be thought of by one.' ],
  'Cross swords': [ 'To disagree; to fight.' ],
  'Cross that bridge when you come to it': [ 'To deal with a problem only when it arises.' ],
  'Cross your fingers': [
    'To hope that things will happen the way you want them to; to wish for good luck or success.'
  ],
  'Crux of the matter': [ 'The most important or critical point.' ],
  'Cry for the moon': [
    'To make an impractical, unreasonable request; to aspire to the impossible.'
  ],
  'Cry in the wilderness': [ 'An unrealistic demand; an unheeded warning.' ],
  'Cry over spilt milk': [
    'To complain about a loss from the past; feeling sorry over a mistake that cannot be changed.'
  ],
  'Cup of tea': [ 'One’s chosen or preferred thing; something that pleases one.' ],
  'Currying favour with': [ 'Behaving obsequiously to ingratiate oneself with someone.' ],
  'Cut and dried': [ 'Ready made; already decided.' ],
  'Cuts corners': [ 'To save money, time, or effort by omitting necessary parts.' ],
  'Cut no ice with me': [ 'Had no influence on me.' ],
  'Cut one short': [ 'To interrupt someone.' ],
  'Cut someone some slack': [ 'Not to criticize too strictly; to be more lenient.' ],
  'Cut the Gordian knot': [
    'Solve a complex problem by a bold stroke; remove the difficulty.'
  ],
  'Cut the mustard': [ 'To perform well; to succeed.' ],
  'Cut to the chase': [ 'To come to the point; get to the important matters.' ],
  'Cut to the quick': [ 'Hurt intensely; deeply offend.' ],
  'Dance to someone’s tune': [ 'Do what others want you to do.' ],
  'Dead ringer': [ 'An exact duplicate.' ],
  'Desperate times call for desperate measures': [
    'When you are extremely desperate you need extremely drastic actions.'
  ],
  'Died in harness': [ 'Worked or served until death.' ],
  'Do a good turn': [ 'Render a service; help someone.' ],
  'Don’t (or never) judge a book by its cover': [ 'We should not judge something by its outward appearance.' ],
  'Done for': [ 'Ruined; beyond help.' ],
  'Donkey’s years': [ 'A very long time.' ],
  'Don’t count your chickens before they hatch': [ 'Don’t make plans based on events that have not yet happened.' ],
  'Don’t put all your eggs in one basket': [ 'Don’t rely on just one plan or resource.' ],
  'Dot one’s i’s and cross one’s t’s': [ 'Be detailed and exact; pay attention to every minor point.' ],
  'Down in the dumps': [ 'Sad and depressed.' ],
  'Down the drain': [ 'Wasted or lost.' ],
  'Down to earth': [ 'Practical and sensible.' ],
  'Drag one’s feet': [
    'To be reluctant to act; do something deliberately at a slow pace.'
  ],
  'Draw a blank': [ 'Fail to find or obtain anything; come up with nothing.' ],
  'Draw a line': [ 'To fix a limit; accept something only up to a certain point.' ],
  'Drew on his fancy': [ 'To use one’s imagination; draw upon creative powers.' ],
  'Drive home': [ 'To emphasize or make something clearly understood.' ],
  'Drive someone up the wall': [ 'To make someone very irritated or angry.' ],
  'Drop names': [
    'To name‐drop; hint at high connections by mentioning famous people.'
  ],
  'Dropping like flies': [
    'Collapsing in large numbers; a great many people or things falling ill or dying.'
  ],
  'Eagle eye': [ 'An eye with sharp visual power; a careful or close watcher.' ],
  'Easier said than done': [ 'More easily talked about than actually accomplished.' ],
  'Eat anyone’s salt': [ 'To be one’s guest; enjoy someone’s hospitality.' ],
  'Eats like a horse': [ 'To eat a lot of food.' ],
  'Egg on': [ 'To encourage or provoke someone.' ],
  'Elbow grease': [ 'A lot of physical effort; hard manual work.' ],
  'Elbow room': [ 'Freedom to act; enough space to move or operate.' ],
  'Ended in a fiasco': [ 'A complete failure.' ],
  'Every cloud has a silver lining': [ 'Every unpleasant situation has a positive side.' ],
  'Every dog has his day': [ 'Everyone enjoys success or good luck at some point.' ],
  'Eye wash': [ 'A deception or pretence.' ],
  'Face the music': [ 'To accept punishment for a mistake; bear the consequences.' ],
  'Fair weather friends': [
    'Friends who are supportive in good times only; convenient allies.'
  ],
  'Fall back on': [ 'To resort to something; seek support out of necessity.' ],
  'Fall flat': [ 'To fail to produce the intended effect; have no impact.' ],
  Fallout: [ 'To quarrel; stop being friendly after an argument.' ],
  'Far cry from': [ 'To be very different from; nothing like.' ],
  'Feather in one’s cap': [ 'An accomplishment to be proud of.' ],
  'Feather one’s own nest': [ 'To enrich oneself improperly; profit by dishonest means.' ],
  'Fed up': [ 'Annoyed; irritated.' ],
  'Feel the pinch': [ 'Have financial problems all of a sudden.' ],
  'Few and far between': [ 'Rare or seldom seen; not frequent or usual.' ],
  'Fight shy of': [ 'To avoid encountering.' ],
  'Finding their feet': [ 'Beginning to understand the work and feeling confident.' ],
  'First and foremost': [ 'Highest priority; the most important aspect.' ],
  'Flash in the pan': [
    'Something whose success is short-lived and unlikely to be repeated.'
  ],
  'Flying off the handle': [ 'To lose one’s temper suddenly; become enraged.' ],
  'Follow suit': [ 'To imitate what others have done.' ],
  'Foot the bill': [ 'To pay for something; pay the cost.' ],
  'Forty winks': [ 'A short nap or sleep during the day.' ],
  'Fought to the bitter end': [ 'Carried on regardless of the consequences.' ],
  'From rags to riches': [ 'To go from very poor to very wealthy.' ],
  'From the bottom of my heart': [ 'Sincerely; with genuine feeling.' ],
  'Full of beans': [ 'Lively and energetic; full of energy.' ],
  'Full of hot air': [ 'Merely loud and angry words but ineffectual.' ],
  'Gall and wormwood': [ 'To feel hatred or bitterness; something extremely unpleasant.' ],
  'Gave the game away': [ 'To leak or reveal a secret unintentionally.' ],
  'Gave vent to something': [ 'To express something forcefully; to let feelings out.' ],
  'Get a foot in the door': [ 'To gain an initial advantage or entry into a position.' ],
  'Get a second wind': [ 'To have a burst of renewed energy after fatigue.' ],
  'Get a taste of your own medicine': [
    'To be given the same (bad) treatment that you have given to others.'
  ],
  'Get down to brass tacks': [ 'To start discussing only the important facts of a situation.' ],
  'Get into hot water': [
    'To get into trouble; to be in a difficult situation in which you can be criticised.'
  ],
  'Get on like a house on fire': [ 'To become friends very quickly.' ],
  'Get on somebody’s nerves': [ 'To irritate or annoy someone.' ],
  'Get out of hand': [ 'To become uncontrollable; to get out of control.' ],
  'Get someone’s goat': [ 'To irritate someone.' ],
  'Get something off one’s chest': [
    'To express something that has been worrying you; get it out in the open.'
  ],
  'Get the axe': [ 'To lose one’s job; be fired.' ],
  'Get the hang of': [ 'To learn how to use; to grasp the main idea.' ],
  'Get the sack': [ 'To be dismissed; lose one’s job.' ],
  'Get up on the wrong side of the bed': [ 'To wake up in a bad mood that persists all day.' ],
  'Get wind of something': [ 'To hear about something; come to know.' ],
  'Get your act together': [
    'To organize your work in a better way; get oneself under control.'
  ],
  'Getting a new lease of life': [
    'A chance to continue living or to become successful or popular again; regain energy.'
  ],
  'Gift of the gab': [
    'Ability to speak eloquently and persuasively; a talent for talking.'
  ],
  'Give a free hand': [
    'To exercise complete control over something; have full freedom of action.'
  ],
  'Give a piece of one’s mind': [ 'To rebuke someone sharply; scold.' ],
  'Give a wide berth to': [ 'To stay well away from; avoid.' ],
  'Give and take': [ 'Adjustment; mutual concessions.' ],
  'Give in': [ 'To yield or surrender.' ],
  'Give it a shot/whirl': [ 'To try out something; have a go.' ],
  'Give me a hand with': [ 'To assist; help someone.' ],
  'Give oneself airs': [ 'To pretend to be superior; act haughty.' ],
  'Give someone the cold shoulder': [ 'To ignore someone deliberately; be unfriendly.' ],
  'Give someone the slip': [ 'To escape from someone; elude.' ],
  'Give the benefit of the doubt': [ 'To accept someone as innocent until proven guilty.' ],
  'Give up the ghost': [ 'To collapse or die; to cease functioning.' ],
  'Go against the grain': [
    'To act in a way contrary to one’s natural inclination or values.'
  ],
  'Go belly up': [ 'To go bankrupt; fail completely.' ],
  'Go cold turkey': [ 'To quit an addictive habit abruptly and completely.' ],
  'Go down in flames': [ 'To fail completely; fail miserably.' ],
  'Go down like a lead balloon': [ 'To be received badly by an audience.' ],
  'Go for a song': [ 'To be sold cheaply.' ],
  'Go for the jugular': [ 'To attack in the most aggressive way; go all out.' ],
  'Go-getter': [ 'A real achiever; an ambitious, energetic person.' ],
  'Go the extra mile': [ 'To exceed expectations; make an extra effort.' ],
  'Go through fire and water': [ 'To experience many dangers in order to achieve something.' ],
  'Go through the roof': [ 'To rise very high.' ],
  'Go to rack and ruin': [ 'To be ruined or deteriorate shockingly.' ],
  'Go to the dogs': [ 'To be ruined or fall into a very poor state.' ],
  'Go to the wall': [ 'To be ruined; to fail completely.' ],
  'Go/start with a bang': [ 'To begin in a very exciting and successful way.' ],
  'God’s ape': [ 'A born fool.' ],
  'Got the green light': [ 'To receive permission to go ahead with something.' ],
  'Grasp at straws': [
    'To make a desperate attempt to succeed when nothing else will work.'
  ],
  'Grease the palm': [ 'To bribe someone discreetly.' ],
  'Great minds think alike': [
    'Said when two people make the same choice or have the same idea.'
  ],
  'Green thumb': [ 'A person with a natural talent for gardening.' ],
  'Green-eyed': [ 'Full of envy; jealous.' ],
  'Grist to the mill': [
    'Something which provides useful advantage; turns to one’s benefit.'
  ],
  'Halcyon days': [ 'A time of peace and happiness; idyllic prosperity.' ],
  'Hale and hearty': [ 'Strong and healthy.' ],
  'Hand in glove': [
    'In a very close association or partnership; working together intimately.'
  ],
  'Hand over fist': [ 'Quickly and continuously (often of earning or losing money).' ],
  'Hang in there': [ 'Don’t give up; persist in a difficult situation.' ],
  'Hang up one’s boots': [ 'To retire from a sport or profession; stop doing it.' ],
  'Hanging by a thread': [ 'To be in a dangerous or precarious situation.' ],
  'Hard and fast': [ 'That cannot be altered; strict and fixed.' ],
  'Hard of hearing': [ 'Partially deaf; having difficulty hearing.' ],
  'Haste makes waste': [ 'Doing things in a hurry results in poor outcomes.' ],
  'Haul over the coals': [ 'To scold someone severely for an error.' ],
  'Have a bee in her bonnet': [ 'To talk and think a lot; to be obsessed with something.' ],
  'Have a chip on one’s shoulder': [ 'To be upset about something in the past; to harbor a grudge.' ],
  'Have a finger in every pie': [ 'To be involved in many varied activities or enterprises.' ],
  'Have a whale of a time': [ 'To have an exceptionally fun or exciting experience.' ],
  'Have an axe to grind': [ 'To have a private interest or ulterior motive.' ],
  'Have bigger fish to fry': [ 'To have more important work to attend to.' ],
  'Have green fingers': [ 'To be naturally gifted at gardening.' ],
  'Have one’s hands full': [ 'To be very busy; have too much to do.' ],
  'Have one’s heart in one’s mouth': [ 'To be extremely frightened and nervous.' ],
  'Have your back to/against the wall': [ 'To be in a desperate situation with very few options.' ],
  'Head in the clouds': [ 'Daydreaming; being absent-minded.' ],
  'Head over heels': [ 'Madly in love; completely enamored.' ],
  'Heads will roll': [ 'Those responsible will be punished or dismissed.' ],
  'Heart and soul': [ 'Completely; with all the effort you can put in.' ],
  'Heart to heart talk': [ 'Frank, candid discussion.' ],
  'Helter-skelter': [ 'In disorderly haste; here and there.' ],
  'Herculean task': [ 'A very difficult, demanding task.' ],
  'High and dry': [ 'Neglected; abandoned in a difficult situation.' ],
  'High and mighty': [ 'Arrogant; puffed up with pride.' ],
  'High time': [ 'Past the appropriate or proper time; overdue.' ],
  'Hit a bad patch': [ 'To experience difficulty; go through a rough period.' ],
  'Hit a brick wall': [ 'To be unable to make any progress; encounter an obstacle.' ],
  'Hit the books': [ 'To study very hard.' ],
  'Hit the ceiling/roof': [ 'To explode in anger; lose one’s temper.' ],
  'Hit the jackpot': [ 'To make money quickly; to find exactly what was sought.' ],
  'Hold one’s tongue': [ 'To be silent; to keep quiet.' ],
  'Hold out an olive branch': [
    'To make a peace offering; to show a desire to end a disagreement.'
  ],
  'Hold the fort': [ 'To take temporary responsibility for a situation.' ],
  'Hold water': [ 'To appear acceptable or reasonable; remain valid.' ],
  'Hold your horses': [ 'To be patient; to wait.' ],
  'Hope against hope': [
    'To nurture an impossible hope; expect success despite little chance.'
  ],
  'Hue and cry': [ 'A noisy expression of protest or anger; loud clamour.' ],
  'I can’t think straight': [ 'To feel unable to think rationally due to overwhelming emotion.' ],
  'I don’t buy it': [ 'I am not convinced; I doubt its truth.' ],
  'Icing on the cake': [ 'Something that makes a good situation even better.' ],
  'Ignorance is bliss': [
    'To remain unaware of things that could cause stress; sometimes it’s better not to know.'
  ],
  'Ill at ease': [ 'To feel uncomfortable or worried in a situation.' ],
  'In a jiffy': [ 'Very quickly; in a moment or two.' ],
  'In a nutshell': [ 'Briefly and concisely; in a few words.' ],
  'In a pickle': [ 'Experiencing a difficult situation; in trouble.' ],
  'In a tight corner/spot': [ 'In a difficult or awkward situation.' ],
  'In apple-pie order': [ 'In perfect order; neatly arranged.' ],
  'In black and white': [ 'In writing; printed or recorded.' ],
  'In cold blood': [ 'Angrily or cruelly, without any emotions; deliberately.' ],
  'In deep water': [ 'In great difficulty; in trouble.' ],
  'In dire straits': [ 'In a very bad or difficult situation.' ],
  'In full swing': [ 'Very active; at the height of activity.' ],
  'In high/good spirits': [ 'Full of hope and enthusiasm; joyful; cheerful.' ],
  'In seventh heaven': [ 'Extremely happy; in delight.' ],
  'In the air': [ 'When an emotion or idea is on everyone’s mind; prevalent.' ],
  'In the blink of an eye': [ 'Within a very short period of time; almost instantly.' ],
  'In the blues': [ 'Cheerless and depressed; low-spirited.' ],
  'In the dark': [ 'To not know something others are aware of.' ],
  'In the doldrums': [ 'In low spirits and despair.' ],
  "In the driver's seat": [ 'In charge or in control of a situation.' ],
  'In the eye of a storm': [ 'In the middle of a difficult situation.' ],
  'In the fast lane': [ 'A life filled with great excitement.' ],
  'In the good books': [ 'In favour with someone.' ],
  'In the heat of the moment': [ 'Acting impulsively under strong emotions.' ],
  'In the long run': [ 'Eventually after a significant time.' ],
  'In the nick of time': [ 'At the very last possible moment.' ],
  'In the pink': [ 'In good health.' ],
  'In the same boat': [ 'Facing the same difficult situation.' ],
  'In the soup': [ 'In trouble or difficulty.' ],
  'In the teeth of': [ 'In spite of opposition or difficulty.' ],
  'In vogue': [ 'Popular or in fashion.' ],
  'Ins and outs': [ 'Full details or complexities of something.' ],
  'It’s Greek to me': [ 'I cannot understand it at all.' ],
  'It’s Raining Cats and Dogs': [ 'It’s raining very heavily.' ],
  'Ivory towers': [ 'Detachment and seclusion from practical affairs.' ],
  'Jump the gun': [ 'Start something too soon or prematurely.' ],
  'Keep a straight face': [ 'To maintain a serious expression despite wanting to laugh.' ],
  'Keep an ear to the ground': [ 'Stay informed about developments.' ],
  'Keep at arm’s length': [ 'Maintain a safe or distant relationship.' ],
  'Keep in touch': [ 'Continue to communicate with someone.' ],
  'Keep one’s head': [ 'Remain calm and composed in difficult situations.' ],
  'Keep under one’s hat': [ 'Keep something secret or confidential.' ],
  'Keep up appearances': [
    'To pretend to be happier or richer so as to conceal the real situation.'
  ],
  'Keep your chin up': [ 'To remain cheerful and hopeful in difficult circumstances.' ],
  'Keep/hold something at bay': [
    'To control something and prevent it from causing you problems or moving closer.'
  ],
  'Kick the bucket': [ 'To die.' ],
  'Kicked up a row': [ 'To make a great fuss or cause a disturbance.' ],
  'Kill two birds with one stone': [ 'To achieve two results with a single effort.' ],
  'Kith and kin': [ 'One’s blood relatives or family members.' ],
  'Know something inside out': [ 'To know everything about something thoroughly.' ],
  'Latin and Greek': [ 'Unable to understand.' ],
  'Lay out': [ 'Spend.' ],
  'Lead someone by the nose': [ 'To completely control or dominate someone.' ],
  'Learn by heart': [ 'To memorize something.' ],
  'Learn/Know the ropes': [ 'To learn how to do a job or task properly.' ],
  'Leave no stone unturned': [
    'To try every possible course of action in order to achieve something.'
  ],
  'Leaves you in the lurch': [ 'To desert someone in difficulties.' ],
  'Left out in cold': [ 'To be ignored.' ],
  'Lend me your ear': [ 'Pay attention to me.' ],
  'Lend someone a hand': [ 'To help or assist, especially voluntarily.' ],
  'Let bygones be bygones': [ 'To forgive and forget past conflicts.' ],
  'Let sleeping dogs lie': [ 'To avoid old controversies and let things remain undisturbed.' ],
  'Let the cat out of the bag': [ 'To reveal a secret carelessly or by mistake.' ],
  'Let the chips fall where they may': [
    'To accept whatever happens without worrying about the consequences.'
  ],
  'Let the grass grow under one’s feet': [ 'To remain idle and do nothing.' ],
  'Let your hair down': [ 'To behave freely and uninhibitedly / to relax and enjoy.' ],
  'Level playing field': [
    'A situation where everyone has a fair and equal chance to succeed.'
  ],
  'Light at the end of the tunnel': [ 'Signs of improvement in a difficult situation.' ],
  'Like a shag on a rock': [ 'Completely alone.' ],
  'Like two peas in a pod': [ 'Things that are very similar in appearance or always together.' ],
  'Lily-livered': [ 'Not brave or cowardly.' ],
  'Lion’s mouth': [ 'A difficult or dangerous situation.' ],
  'Live from hand to mouth': [
    'To survive with just enough money, without saving anything extra.'
  ],
  'Lock, stock and barrel': [ 'Completely; including all or every part of something.' ],
  'Look before you leap': [ 'Think carefully about the consequences before acting.' ],
  'Look down your nose at': [ 'Regard with contempt or consider someone inferior.' ],
  'Loosen the purse strings': [ 'To increase the money available for expenditure.' ],
  'Lose face': [ 'To become embarrassed or lose respect.' ],
  'Lose one’s head': [ 'To panic or lose self-control.' ],
  'Lose your marbles': [ 'To become mentally confused or insane.' ],
  'Made a clean breast of': [ 'To admit or confess something fully.' ],
  'Made light of': [ 'To treat something lightly or with little importance.' ],
  'Maiden speech': [ 'The first speech ever given by someone.' ],
  'Make a beeline for': [ 'To go straight to something.' ],
  'Make a hash of': [ 'To do something very badly or make a mess of it.' ],
  'Make a quick buck': [ 'To earn money quickly and easily.' ],
  'Make head or tail of something': [ 'To understand or figure something out.' ],
  'Make no bones about': [ 'To state something clearly and without hesitation.' ],
  'Make one’s blood boil': [ 'To become extremely angry.' ],
  'Make one’s mark': [ 'To distinguish oneself or attain recognition.' ],
  'Make up with (someone)': [ 'To settle differences and become friendly again.' ],
  'Making hay while the sun shines': [ 'To take advantage of a favorable opportunity.' ],
  'Mealy mouthed': [
    'To be afraid to state something directly or to speak insincerely.'
  ],
  'Method to my madness': [ 'A reason or purpose behind apparently crazy or random actions.' ],
  'Milk and water': [ 'Weak ideas or statements.' ],
  'Much ado about nothing': [ 'Making a big fuss over a small matter.' ],
  'Neck of the woods': [ 'Neighbourhood or region.' ],
  'New kid on the block': [ 'Someone new to a place or activity.' ],
  'Nine days’ wonder': [ 'A short-lived sensation.' ],
  'Nip in the bud': [ 'To stop something at the start before it develops.' ],
  'No love lost between': [ 'There is intense dislike or people are not on good terms.' ],
  'Not fit to hold a candle': [ 'Inferior to or cannot be compared to another.' ],
  'Not hold water': [ 'To not seem reasonable or believable.' ],
  'Not mince words': [ 'To be blunt or frank.' ],
  'Not to look a gift horse in the mouth': [ 'To not find fault with what is received as a gift.' ],
  'Off and on / On and Off': [ 'Occasionally or periodically.' ],
  'It’s a small world': [ 'People often meet unexpectedly or have common acquaintances.' ],
  'Lock horns': [ 'To get into an argument or fight.' ],
  "Make one's flesh crawl/creep": [ 'To be very frightened or disgusted.' ],
  'Mouth watering': [ 'Appealing to taste; looks or smells delicious.' ],
  'Move heaven and earth': [ 'Do everything possible to achieve something.' ],
  'Not one’s cup of tea': [ 'Not something one likes or enjoys.' ],
  'Null and void': [ 'Invalid; without legal force.' ],
  'Of the first water': [ 'Of the best quality.' ],
  'Off the hook': [ 'No longer in difficulty or trouble.' ],
  'On a roll': [ 'To be experiencing a period of repeated success.' ],
  'On cloud nine': [ 'Extremely happy and excited.' ],
  'On tenterhooks': [ 'In suspense or anxious.' ],
  'On the back burner': [ 'To temporarily not deal with something as it is less urgent.' ],
  'On the ball': [ 'To be alert and quick to respond.' ],
  'On the breadline': [ 'Very poor or living at a subsistence level.' ],
  'On the brink/verge of': [ 'At the edge of a major change or event.' ],
  'On the cards': [ 'Likely to happen or probable.' ],
  'On the face of it': [ 'According to what appears on the surface.' ],
  'On the horizon': [ 'An event that is likely to happen soon.' ],
  'On the same page': [ 'To be in agreement or think in the same way.' ],
  'On the spur of the moment': [ 'Acting impulsively without thinking.' ],
  'On the wane': [ 'On the decline or decreasing.' ],
  'On thin ice': [ 'In a dangerous or risky situation.' ],
  'Once and for all': [ 'To bring to an end conclusively or finally.' ],
  'Once bitten, twice shy': [ 'An unpleasant experience makes one cautious for future.' ],
  'Once in a blue moon': [ 'Rarely or very infrequently.' ],
  'Out of date': [ 'Out of date.' ],
  'Out of sorts': [ 'To be unwell or slightly sick.' ],
  'Out of the blue': [ 'Completely unexpectedly.' ],
  'Out of the question': [ 'Impossible.' ],
  'Out of the woods': [ 'Out of the woods.' ],
  'Over the moon': [ 'Extremely happy or delighted.' ],
  'Pandora’s Box': [ 'A source of many unforeseen problems or trouble.' ],
  'Part and parcel': [ 'An essential or integral element.' ],
  'Pass the buck': [ 'To refuse responsibility or blame someone else.' ],
  'Pass the hat round/around': [ 'To collect money.' ],
  'Pat on the back': [ 'To praise or approve for doing something good.' ],
  'Pay lip service': [ 'To pretend to agree or say something without meaning it.' ],
  'Penny wise and pound foolish': [ 'Careful with trivial matters but wasteful in large issues.' ],
  'Pig in a poke': [ 'Something bought without examining properly.' ],
  'Pillar to post': [ 'Moving from one place to another repeatedly.' ],
  'Pipe dream': [ 'A dream or idea that is unlikely to happen.' ],
  'Play devil’s advocate': [ 'To argue the opposite just for the sake of argument.' ],
  'Play it by ear': [ 'To do something without special preparation or to improvise.' ],
  'Play one’s ace': [ 'To use one’s best weapon or resource.' ],
  'Play to the gallery': [ 'To seek to win approval or to impress others.' ],
  'Play with fire': [ 'To do something dangerous or take a foolish risk.' ],
  'Played ducks and drakes': [ 'To squander or waste recklessly.' ],
  'Pocket an insult': [ 'To bear an insult quietly or tolerate it without protest.' ],
  'Point-blank': [ 'Directly or very close.' ],
  'Poke one’s nose': [ 'To interfere or meddle in others’ affairs.' ],
  'Pour/Throw cold water': [ 'To discourage by showing indifference.' ],
  'Pull someone up': [ 'To criticize or reprimand someone.' ],
  'Pull someone’s leg': [ 'To play a joke on or tease someone.' ],
  'Pull strings': [ 'To use personal influence.' ],
  'Pull the plug': [ 'To stop something from happening or continuing.' ],
  'Pull up your socks': [ 'To put in extra effort or improve performance.' ],
  'Pull yourself together': [ 'To calm yourself down and behave appropriately.' ],
  'Pulled all the stops': [ 'To do something with maximum effort or ability.' ],
  'Put off': [ 'To postpone or delay something.' ],
  'Put one’s foot down': [ 'To take a firm stand or assert authority.' ],
  'Put two and two together': [ 'To deduce or reason logically from facts.' ],
  'Putting the cart before the horse': [ 'To do things in the wrong order.' ],
  'Queer pitch': [ 'To spoil somebody’s chance of doing something.' ],
  'Rained on the bride’s parade': [ 'To spoil and ruin someone’s happiness or plans.' ],
  'Raise a few eyebrows': [ 'To cause surprise or mild shock in others.' ],
  'Raise the alarm': [ 'To warn of a dangerous situation.' ],
  'Ran in the groove': [ 'To move in harmony or smoothly.' ],
  'Rat race': [ 'Fierce competition for power or success.' ],
  'Read between the lines': [ 'To find a hidden meaning not explicitly stated.' ],
  'Red-tape': [ 'Official procedures causing delay or excessive bureaucracy.' ],
  'Rest on one’s laurels': [ 'To be satisfied with past success and not make further effort.' ],
  'Ring a bell': [ 'To sound familiar or remind you of something.' ],
  'Rise like a phoenix': [ 'To become successful again or to emerge with new life.' ],
  'Rise to the occasion': [ 'To deal successfully with a difficult situation.' ],
  'Rock the boat': [ 'To disturb a stable situation.' ],
  'Roll up your sleeves': [ 'To get ready to do something difficult or hard work.' ],
  'Rub somebody the wrong way': [ 'To irritate or annoy someone.' ],
  'Run out of steam': [ 'To lose impetus or enthusiasm and stop doing something.' ],
  'Rule the roost': [ 'To dominate or make all the decisions; be in complete control.' ],
  'Salt of the earth': [ 'A good, reliable, honest person.' ],
  Scapegoats: [ 'People who are blamed or punished for others’ misdeeds.' ],
  'Scrape the bottom of the barrel': [ 'To use one’s last and weakest resource.' ],
  'See eye to eye': [ 'To be in full agreement with someone.' ],
  'See the light of day': [ 'To become publicly known or visible.' ],
  'Selling like hot cakes': [ 'Selling very quickly and in large numbers.' ],
  'Separate the wheat from the chaff': [ 'To sort out the valuable from the worthless.' ],
  'Shake off': [ 'To get rid of something.' ],
  'Sharp as a tack': [ 'Extremely intelligent and mentally active.' ],
  'Shed crocodile tears': [ 'To pretend to be sad or show false sympathy.' ],
  'Shot in the dark': [ 'A random attempt with little chance of success.' ],
  'Sit on the fence': [ 'To remain neutral or undecided between two options.' ],
  'Snake in the grass': [ 'An unreliable and deceitful person.' ],
  'Snowed under': [ 'Busy.' ],
  'Soft option': [ 'Easy and agreeable option.' ],
  'Sought after': [ 'In great demand.' ],
  'Sow wild oats': [ 'To waste time by doing foolish things, especially in youth.' ],
  'Speak of the devil': [ 'The person we were just talking about showed up.' ],
  'Speaks volumes': [ 'Gives enough proof without using words.' ],
  'Spick and span': [ 'Very neat, clean, or tidy.' ],
  'Spill the beans': [ 'Disclose the secrets accidentally.' ],
  'Spin one’s wheels': [ 'Expel much effort for little or no gain.' ],
  'Split one’s sides (laughing)': [ 'Be extremely amused.' ],
  'Spread like wildfire': [ 'Spread rapidly.' ],
  'Slap on the wrist': [ 'Mild punishment.' ],
  'Sleep on it': [ 'Delay making a decision until the next day.' ],
  'Square peg in a round hole': [ 'A misfit in the environment.' ],
  'Stab someone in the back': [ 'Betray someone.' ],
  'Stand by': [ 'To support or remain loyal to someone.' ],
  'Steal someone’s thunder': [ 'Take credit for something someone else did.' ],
  'Start/set/get the ball rolling': [ 'To start doing something.' ],
  'Stick to one’s guns': [
    'Maintain one’s own opinion; not change one’s decision despite opposition.'
  ],
  'Steer clear of': [ 'Avoid someone or something because it is dangerous for you.' ],
  'Still waters run deep': [
    'Have passion or great intelligence underneath a calm expression.'
  ],
  'Stir up a hornet’s nest': [ 'Cause anger in many people or raise controversy.' ],
  'Straight from the horse’s mouth': [ 'Receive information directly from the person involved.' ],
  'Strain every nerve': [ 'Work very hard.' ],
  'Strike while the iron is hot': [
    'To act at the right time or grab a favourable opportunity promptly.'
  ],
  'Struck several bad patches': [ 'Had many professional difficulties.' ],
  'Suit you to a T': [ 'To be ideal or perfectly appropriate for one.' ],
  'Sweep under the carpet': [
    'To hide a problem or try to keep it secret instead of dealing with it.'
  ],
  'Swollen-headed': [ 'Pride.' ],
  'Sword of Damocles': [ 'Imminent danger.' ],
  'Take a cue from someone': [ 'Learn and act by being strongly influenced by someone.' ],
  'Take exception to': [ 'To object strongly.' ],
  'Take heart': [ 'To take courage or to gain confidence.' ],
  'Take to one’s heels': [ 'To run away or flee in fear.' ],
  'Take with a pinch/grain of salt': [ 'Not believe completely something that you are told.' ],
  'Take the bull by the horn': [
    'To face a difficult or dangerous situation in a very direct or confident way.'
  ],
  'Takes after': [ 'To be similar in appearance.' ],
  'Taking a toll on': [
    'To harm or damage someone or something, especially in a gradual way.'
  ],
  'Talked over': [ 'Discussed.' ],
  'Talking through her hat': [ 'Talking nonsense.' ],
  'The bad egg': [ 'A dishonest or ill-behaved person.' ],
  'The early bird catches the worm': [ 'One who arrives first gets the best chance at success.' ],
  'The elephant in the room': [ 'A big problem everyone is ignoring or afraid to talk about.' ],
  'The grass is greener on the other side': [
    'Other people always seem to be in a better situation, although it might not be true.'
  ],
  'Teething problems': [ 'Problems at the start of a new project.' ],
  'The green-eyed monster': [ 'Jealousy.' ],
  'The last straw': [
    'Final problem in a series of difficulties that makes a situation unbearable.'
  ],
  'The Lion’s share': [ 'The biggest and best part of a whole.' ],
  'The man in the street': [ 'The ordinary man.' ],
  'The pot calling the kettle black': [ 'People are guilty of the very fault they identify in others.' ],
  'The pros and cons': [ 'For and against; advantages and disadvantages.' ],
  'The seamy side': [ 'The unpleasant aspects.' ],
  'The thin end of the wedge': [ 'Start of harmful development; beginning of something bad.' ],
  'The whys and wherefores': [ 'Underlying reasons or causes of something.' ],
  'Thick as thieves': [ 'Having a close friendship.' ],
  'Threw a spanner': [ 'Do something that prevents a plan or activity from succeeding.' ],
  'Through thick and thin': [ 'Support under all circumstances.' ],
  'Throw caution to the wind': [ 'Behave recklessly without worrying about the risk.' ],
  'Throw in the towel': [ 'Acknowledge defeat or surrender.' ],
  'Tickled pink': [ 'Very pleased.' ],
  'Tie the knot': [ 'Get married.' ],
  'To accept the gauntlet': [ 'To accept or respond to a challenge.' ],
  'To air dirty linen in public': [ 'To discuss private affairs in public.' ],
  'To be devil’s advocate': [ 'To raise a counter argument just for the sake of it.' ],
  'To be fair and square': [ 'To be honest; according to the rules.' ],
  'To be in a fix': [ 'To be in a difficult situation.' ],
  'To be on pins and needles': [ 'To be in an agitated state of suspense.' ],
  'To be on the horns of a dilemma': [ 'To be in a difficult situation or choice.' ],
  'To be taken aback': [ 'To be surprised or shocked.' ],
  'To beat a retreat': [ 'To run away in fear; to withdraw.' ],
  'To beat the clock': [ 'To perform a task within the time limit.' ],
  'To blow hot and cold': [ 'To be friendly and unfriendly at the same time; vacillating.' ],
  'To bring to light': [ 'To reveal clearly.' ],
  'To burn one’s fingers': [ "To suffer unpleasant consequences as a result of one's actions." ],
  'To burn the candle at both ends': [ 'To work excessively hard or keep busy all the time.' ],
  'To call a spade a spade': [
    'To be frank or say the truth about something, even if it is not polite.'
  ],
  'To clip one’s wings': [ 'To restrict someone’s freedom.' ],
  'To come out in the open': [ 'To become public or evident.' ],
  'To cry wolf': [ 'To raise a false alarm or ask for help when you do not need it.' ],
  'To cudgel one’s brains': [ 'To think hard.' ],
  'To cut a sorry figure': [ 'Created a wrong impression.' ],
  'To eat humble pie': [ 'To accept defeat or suffer humiliation.' ],
  'Throw up the sponge': [ 'To surrender; to acknowledge defeat.' ],
  'Till the cows come home': [ 'For a very long time.' ],
  'Tit for tat': [ 'To do harm as done to you; counter attack.' ],
  "To cut one's coat according to one's cloth": [ "To live within one's means." ],
  'To die in harness': [ 'To continue occupation till death.' ],
  'To draw the long bow': [ 'To exaggerate.' ],
  'To end in smoke': [ 'To come to nothing; end without any practical result.' ],
  'To feel at home': [ 'To feel easy and comfortable.' ],
  'To fight tooth and nail': [ 'To make every possible effort; to fight furiously and fiercely.' ],
  'To fish in troubled waters': [ 'To profit out of disturbance; to get benefit in bad situation.' ],
  'To flog/beating a dead horse': [
    'To attempt the impossible; waste energy on an unalterable situation.'
  ],
  'To foam at one’s mouth': [ 'To get very angry; to be enraged and shout.' ],
  'To get away with': [ 'To escape from something.' ],
  'To get cold feet': [
    'To experience nervousness or anxiety before one attempts to do something.'
  ],
  'To gird up the loins': [ 'To prepare for hard work or a difficult situation.' ],
  'To give the devil his due': [
    'To give encouragement or credit to an enemy; to give credit to a notorious person.'
  ],
  'To go bananas': [ 'To become very excited or angry.' ],
  'To go scot-free': [ 'To escape without punishment; unpunished.' ],
  'To go the whole hog': [ 'To do something as completely as possible.' ],
  'To go/run around in circles': [
    'To waste one’s time and energy doing trivial things; to keep doing something without achieving much.'
  ],
  'To hail from': [ 'To come from a particular place.' ],
  'To have a gut feeling': [ 'Strong instinct or intuition.' ],
  'To have second thoughts': [ 'To reconsider.' ],
  'To have something up one’s sleeve': [ 'To have a secret plan; have an alternative plan.' ],
  'To have a sigh of relief': [
    'To suddenly feel very happy because something unpleasant has not happened or has ended.'
  ],
  'To hit below the belt': [
    'To attack in an unfair manner; contrary to the principles of fairness.'
  ],
  'To hammer out': [ 'To reach an agreement after long discussion.' ],
  "To his heart's content": [ 'As much as one wants.' ],
  'To judge a book by its cover': [ 'To evaluate people’s worth by their outward appearance.' ],
  'To jump on the bandwagon': [
    'To follow popular trends; to get involved in an activity because it is likely to succeed.'
  ],
  'To keep an eye on': [ 'To watch someone or something carefully; to be cautious.' ],
  'To keep one’s temper': [ 'To remain calm.' ],
  'To let someone off': [ 'To release someone from blame.' ],
  'To lose ground': [ 'Becoming less acceptable.' ],
  'To make a mountain out of a molehill': [
    'To give great importance to little things; exaggerate a minor problem.'
  ],
  'To make amends': [ 'To compensate; to correct a mistake.' ],
  'To keep the wolf away from the door': [ 'To keep away extreme poverty; to earn just enough for a living.' ],
  'To keep under wraps': [ 'To keep secret.' ],
  'To hit the sack': [ 'To prepare for sleep; to go to bed.' ],
  'To make both ends meet': [
    'To live within one’s income; manage expenses with just enough funds.'
  ],
  'To make up one’s mind': [ 'To decide what to do; decide firmly.' ],
  'To meet one’s Waterloo': [
    'To experience defeat; to be defeated by someone who is too strong for you.'
  ],
  'To miss the boat': [ 'To miss an opportunity; lose an opportunity.' ],
  'To paddle one’s own canoe': [ 'Manage independently; to work independently.' ],
  'To pay through the nose': [ 'To pay an extremely high price.' ],
  'To pick holes in': [ 'To criticize someone; finding fault with.' ],
  'To play fast and loose': [ 'To act in an unreliable way; to be playful.' ],
  'To play second fiddle': [
    'Position has lesser importance than anybody else; take a subordinate role.'
  ],
  'To pour oil on troubled water': [ 'To calm a dispute.' ],
  'To put up with someone': [ 'Tolerate.' ],
  'To raise a dust': [ 'To cause disruption or confusion.' ],
  'To set the Thames on fire': [ 'To do a heroic deed; do wonderful or exciting things.' ],
  'To show a clean pair of heels': [ 'To escape; ran away.' ],
  'To smell a rat': [ 'Suspect a trick or deceit; detect something wrong.' ],
  'To prime the pump': [ 'Encourage the growth or action of something.' ],
  'To put a spoke in one’s wheel': [
    'To put a difficulty in the way of progress; thwart in the execution of the plan.'
  ],
  'To speak one’s mind': [ 'To express one’s thoughts; to voice one’s thoughts plainly.' ],
  'To stand on one’s feet': [ 'To be strong and independent.' ],
  'To stand one’s ground': [ 'Refused to yield; refuse to change your opinion.' ],
  'To stick one’s neck out': [ 'To take a risk.' ],
  'To take a back seat': [ 'To become less important or to give up control over things.' ],
  'To take a stock of': [
    'To assess and evaluate before taking a decision; to think carefully.'
  ],
  'To take French leave': [
    'Absenting oneself without permission; leave without any intimation.'
  ],
  'To take pains': [ 'To make efforts; try hard.' ],
  'To take to heart': [
    'To be greatly affected by; to consider something very seriously.'
  ],
  'To take to task': [ 'To be punished; to be rebuked or scolded.' ],
  'To throw dust in one’s eyes': [ 'To deceive; to mislead or confuse.' ],
  'To toe the line': [ 'To follow the lead; follow the rules strictly.' ],
  'To turn a deaf ear': [ 'Disregard; refuse to obey; to be indifferent; neglect.' ],
  'To turn over a new leaf': [ 'To change one’s behaviour for better; to begin again.' ],
  'To win laurels': [ 'To achieve honours and glory.' ],
  'Too many irons in the fire': [ 'Engaged in too many enterprises at the same time.' ],
  'Took a leap in the dark': [
    'Took a risk; to do something without being certain of the outcome and result.'
  ],
  'Tricks of the trade': [ 'Special skills or knowledge.' ],
  'True colours': [ 'Real character; personality.' ],
  'To take for granted': [ 'To assume something without question.' ],
  'To take into account': [ 'To consider; to keep in mind.' ],
  'To take one’s hat off (to someone)': [ 'To admire or respect.' ],
  'To the manner born': [ 'Naturally suited for something.' ],
  'To wrangle over an ass’s shadow': [ 'To fight over trifles.' ],
  'Toffee-nosed': [ 'Snobbish; arrogant.' ],
  'Took exception (to)': [ 'Objected; felt offended.' ],
  'Took to their heels': [ 'Ran away.' ],
  'Turn a blind eye': [ 'To ignore a situation, facts, or reality.' ],
  'Turn up one’s nose': [ 'Treat other people with contempt; despise.' ],
  'Twist someone’s arm': [
    'Force someone to do something by making it hard for them to refuse; persuade someone.'
  ],
  'Two heads are better than one': [
    'It’s helpful to have the advice/opinion of a second person; two people working together can achieve more than a person working alone.'
  ],
  'Under a cloud': [ 'Under suspicion.' ],
  'Under duress': [ 'Under pressure; compulsion.' ],
  'Under his nose': [ 'Right in front of someone, often without them noticing.' ],
  'Under the weather': [
    'To not feel well; to feel sick or unhealthy; to be in low spirits'
  ],
  'Up a blind alley': [
    'Following a course of action that is certain to lead to an undesirable outcome.'
  ],
  'Up in arms': [
    'To be angry; protesting vigorously about something; in rebellion.'
  ],
  'Up to the mark': [ 'As good as the others; up to the required standard.' ],
  'Upset someone’s applecart': [ 'To cause trouble, especially by spoiling someone’s plans.' ],
  'Vanish/disappear into thin air': [ 'Disappear suddenly.' ],
  'Vote with your feet': [
    'Show their disapproval; to show that you do not support something.'
  ],
  'Walk the tightrope': [
    'Be very cautious; to be in a precarious situation requiring caution and skill.'
  ],
  'Walking on thin ice': [ 'Doing something risky.' ],
  'Water under the bridge': [
    'Something that can’t be changed anymore; something happened in the past and is no longer important or worth arguing about.'
  ],
  'Weal and woe': [
    'Good times and bad times; joys and sorrows; in prosperity and adversity.'
  ],
  'Wear and tear': [ 'Damage.' ],
  'Wears his heart on his sleeve': [ 'Expresses his feelings openly; to show your true emotions.' ],
  'Weather the storm': [ 'Survive a period of difficulty.' ],
  'When it rains, it pours': [ 'Problems seem to happen together.' ],
  'When pigs fly': [ 'Something that is impossible.' ],
  'When the crunch comes': [
    'A critical moment near the end when a decisive action is needed.'
  ],
  'Where there’s a will, there’s a way': [
    'If you have a strong determination to do something, then you can find a method to do it.'
  ],
  'Whistle in the dark': [ 'Pretend to be unafraid; try to keep up his confidence.' ],
  'White elephant': [ 'Costly and troublesome possession useless to its owner.' ],
  'Whole nine yards': [ 'The entirety of something; everything all the way.' ],
  'Wild goose chase': [
    'A worthless hunt or chase; futile search; unprofitable adventure.'
  ],
  'Will-o-the-wisp': [
    'Something that is impossible to get or achieve; unreal imagining.'
  ],
  'Went to the winds': [ 'Dissipated.' ],
  'With open arms': [ 'Warmly welcome.' ],
  'Word of mouth': [ 'Through the verbal sharing of information.' ],
  'Worth its weight in gold': [ 'Very useful, valuable, or important.' ],
  'Yeoman service': [ 'Excellent service; useful help in need.' ],
  'Your guess is as good as mine': [ 'Have no idea of the answer.' ],
  'Zero tolerance': [ 'A policy of not allowing any violations of a rule or law.' ],
  'Zip your lip': [ 'Keep quiet about something.' ],
  'Turn down': [ 'To reject or refuse.' ],
  'Turn turtle': [ 'To overturn or capsize.' ],
  'Wash one’s hands off something': [ 'To withdraw from responsibility; disclaim connection with.' ]
}

MM_OWS_DATA = {
  "A place where animals are slaughtered for consumption as food": [
    "Abattoir"
  ],
  "To reduce to a shorter form intended to stand for the whole": [
    "Abbreviation"
  ],
  "To give up one's authority or throne": [
    "Abdicate"
  ],
  "Act of giving up (renouncing) the throne": [
    "Abdication"
  ],
  "Formally put an end to a system, practice, or institution": [
    "Abolish"
  ],
  "The original inhabitants/natives of a country": [
    "Aborigines"
  ],
  "To increase the speed": [
    "Accelerate"
  ],
  "A person who helps another to commit a crime or to do something morally wrong": [
    "Accomplice"
  ],
  "Sharp, bitter, or harsh in temper, language, etc.": [
    "Acerbic"
  ],
  "The scientific study of sound": [
    "Acoustics"
  ],
  "To decide and state officially in court that somebody is not guilty of a crime": [
    "Acquit"
  ],
  "An entertainer who performs difficult physical feats": [
    "Acrobat"
  ],
  "An abbreviation formed from the initial letters of other words and pronounced as a word": [
    "Acronym"
  ],
  "Fear of great heights": [
    "Acrophobia"
  ],
  "The ability to make good judgments and take quick decisions": [
    "Acumen"
  ],
  "A person who is physically dependent on a substance/harmful drugs": [
    "Addict"
  ],
  "The period between the beginning of puberty and adulthood": [
    "Adolescence"
  ],
  "Growing/existing/living in air": [
    "Aerial"
  ],
  "Concerned with beauty or the appreciation of beauty": [
    "Aesthetic"
  ],
  "A list of items to be discussed at a meeting": [
    "Agenda"
  ],
  "To increase the importance, position or wealth": [
    "Aggrandize"
  ],
  "Extreme mental or physical suffering": [
    "Agony"
  ],
  "Study of chemistry in a medieval fashion": [
    "Alchemy"
  ],
  "Fear of pain": [
    "Algophobia"
  ],
  "A person belonging to a foreign country": [
    "Alien"
  ],
  "The money paid to former wife, husband or partner when the marriage is ended": [
    "Alimony"
  ],
  "A story, play, picture, etc. in which each character/event is a symbol representing an idea/a quality": [
    "Allegory"
  ],
  "Words that begin with the same letter, syllable or sound": [
    "Alliteration"
  ],
  "The school or college in which one has been educated": [
    "Alma Mater"
  ],
  "A publication containing astronomical or meteorological annual calendar that contains important dates and time": [
    "Almanac"
  ],
  "A table or flat surface where offerings are made to a deity": [
    "Altar"
  ],
  "The height above sea level": [
    "Altitude"
  ],
  "Someone who makes charitable donations intended to the welfare of other people": [
    "Altruist"
  ],
  "One who plays for pleasure rather than as a profession": [
    "Amateur"
  ],
  "Able to use the left hand and right hand equally well": [
    "Ambidextrous"
  ],
  "Capable of being understood in either of two or more possible senses": [
    "Ambiguous"
  ],
  "One who has the qualities like shyness and openness at the same time": [
    "Ambivert"
  ],
  "Walk or move at a slow, relaxed pace": [
    "Amble"
  ],
  "Make (something bad or unsatisfactory) better": [
    "Ameliorate"
  ],
  "A partial or total loss of memory": [
    "Amnesia"
  ],
  "An official pardon": [
    "Amnesty"
  ],
  "Not following any moral rules and not caring about right/wrong": [
    "Amoral"
  ],
  "Animals that can live both on land and in water": [
    "Amphibians"
  ],
  "A similarity between like features of two things, on which a comparison may be based": [
    "Analogy"
  ],
  "A person who believes that laws and governments are not necessary": [
    "Anarchist"
  ],
  "A situation in a country, an organization, etc. in which there is no government, order/control": [
    "Anarchy"
  ],
  "A person who presents a radio/television programme": [
    "Anchor"
  ],
  "Belonging to the long past": [
    "Ancient"
  ],
  "A short, interesting or amusing story about a real person or an event": [
    "Anecdote"
  ],
  "A medical specialist who administers drugs for relieving pain during surgery": [
    "Anesthetist"
  ],
  "A strong dislike or hostility": [
    "Animosity"
  ],
  "To destroy completely": [
    "Annihilate"
  ],
  "The date on which an event happened in some previous year": [
    "Anniversary"
  ],
  "Whose names are not known": [
    "Anonymous"
  ],
  "Obsessive desire to lose weight by refusing to eat": [
    "Anorexia"
  ],
  "A collection of poems, stories, etc. that have been written by different people and published together in a book": [
    "Anthology"
  ],
  "One who studies the evolution of mankind": [
    "Anthropologist"
  ],
  "The study of human race, especially of its origin, development, customs and beliefs": [
    "Anthropology"
  ],
  "A medicine to nullify the effect of poison or another medicine": [
    "Antidote"
  ],
  "Strong dislike between two persons": [
    "Antipathy"
  ],
  "One who studies/deals antique things": [
    "Antiquarian"
  ],
  "The exact opposite": [
    "Antithesis"
  ],
  "A policy that segregates people on the basis of race": [
    "Apartheid"
  ],
  "Showing or feeling no interest, enthusiasm, or concern": [
    "Apathetic"
  ],
  "The feeling of not being interested in or enthusiastic": [
    "Apathy"
  ],
  "A place where bees are kept": [
    "Apiary"
  ],
  "A person who renounces a religious or political belief or principle": [
    "Apostate"
  ],
  "A person who works for an expert to learn a trade": [
    "Apprentice"
  ],
  "Being afraid of water or being near water": [
    "Aquaphobia"
  ],
  "A glass tank where fish and water plants are kept": [
    "Aquarium"
  ],
  "Animals and plants growing or living in, or near water": [
    "Aquatic"
  ],
  "A person who is chosen to settle a disagreement": [
    "Arbitrator"
  ],
  "One who studies human Antiquities": [
    "Archaeologist"
  ],
  "The study of human history and prehistory through the excavation of sites": [
    "Archaeology"
  ],
  "No longer in use": [
    "Archaic"
  ],
  "A large body of water with many islands": [
    "Archipelago"
  ],
  "The place where public, government or historical records are kept": [
    "Archive"
  ],
  "A place where fights take place": [
    "Arena"
  ],
  "A government by the nobles": [
    "Aristocracy"
  ],
  "A military structure where arms and ammunition and other military equipment are stored": [
    "Arsenal"
  ],
  "Deliberately and meticulously set something on fire": [
    "Arson"
  ],
  "A criminal who illegally sets fire to property": [
    "Arsonist"
  ],
  "Fear of fire": [
    "Arsonphobia"
  ],
  "Good at expressing ideas, feelings clearly in words": [
    "Articulate"
  ],
  "One who practices one of the fine arts": [
    "Artist"
  ],
  "One who denies oneself ordinary bodily pleasures": [
    "Ascetic"
  ],
  "To attribute a cause or characteristic to something": [
    "Ascribe"
  ],
  "The science of foretelling events by mapping stars": [
    "Astrology"
  ],
  "A person engaged in or trained for spaceflight": [
    "Astronaut"
  ],
  "The scientific study of celestial bodies like sun, moon, stars, planets, etc.": [
    "Astronomy"
  ],
  "Place that provides refuge": [
    "Asylum"
  ],
  "One who doesn\"t believe in the existence of God": [
    "Atheist"
  ],
  "That can be heard clearly": [
    "Audible"
  ],
  "One who makes an official examination of accounts/financial records": [
    "Auditor"
  ],
  "A building where an audience sits": [
    "Auditorium"
  ],
  "Made or done in the traditional or original way": [
    "Authentic"
  ],
  "The life history of a person written by himself": [
    "Autobiography"
  ],
  "A system of government of a country in which one person has complete power": [
    "Autocracy"
  ],
  "A ruler who has complete power": [
    "Autocrat"
  ],
  "A self-governing country or region": [
    "Autonomy"
  ],
  "An official examination of a dead body by a doctor in order to discover the cause of death": [
    "Autopsy"
  ],
  "A mass of snow, ice and rocks falling rapidly down a mountainside": [
    "Avalanche"
  ],
  "Insatiable desire for wealth": [
    "Avarice"
  ],
  "Having an extreme desire for wealth": [
    "Avaricious"
  ],
  "A place for keeping the birds in a confined space": [
    "Aviary"
  ],
  "A rule/principle that most people believe to be true": [
    "Axiom"
  ],
  "A man having no hair on the scalp": [
    "Bald"
  ],
  "A large bundle bound for storage or transport": [
    "Bale"
  ],
  "A poem that tells a story and has a regular rhythm and rhyme scheme": [
    "Ballad"
  ],
  "One who is unable to pay his debts": [
    "Bankrupt"
  ],
  "Jokes and funny remarks amongst friends": [
    "Banter"
  ],
  "An instrument used for measuring atmospheric pressure": [
    "Barometer"
  ],
  "Housing for soldiers": [
    "Barracks"
  ],
  "A cylindrical container": [
    "Barrel"
  ],
  "A group of guns or missile launchers operated together at one place": [
    "Battery"
  ],
  "Something of monstrous size or power": [
    "Behemoth"
  ],
  "A person who is fond of fighting": [
    "Bellicose"
  ],
  "The sound made by the crocodile": [
    "Bellow"
  ],
  "One who helps people by giving them money or other aid": [
    "Benefactor"
  ],
  "A group of girls/boys/birds etc.": [
    "Bevy"
  ],
  "A list of the books referred to in a scholarly work": [
    "Bibliography"
  ],
  "Preoccupation with the acquisition and possession of books": [
    "Bibliomania"
  ],
  "A person who loves or collects books": [
    "Bibliophile"
  ],
  "A thing which happens every two years": [
    "Biennial"
  ],
  "A person who is intolerant towards those holding different opinions": [
    "Bigot"
  ],
  "A person who can speak only two languages": [
    "Bilingual"
  ],
  "The story of a person’s life written by somebody else": [
    "Biography"
  ],
  "Study of living organisms": [
    "Biology"
  ],
  "The removal of tissue from the body of somebody who is ill for examination": [
    "Biopsy"
  ],
  "Words uttered impiously about God or sacred things": [
    "Blasphemy"
  ],
  "The sound made by sheep": [
    "Bleat"
  ],
  "One who does not follow the usual rules of social life": [
    "Bohemian"
  ],
  "Huge fire for celebration": [
    "Bonfire"
  ],
  "An avid book reader": [
    "Bookworm"
  ],
  "One who is well-versed in the knowledge of plants": [
    "Botanist"
  ],
  "The scientific study of plants and their structure": [
    "Botany"
  ],
  "A broad road bordered with trees": [
    "Boulevard"
  ],
  "An arrangement of flowers that is usually given as a present": [
    "Bouquet"
  ],
  "A small shop that sells fashionable clothes": [
    "Boutique"
  ],
  "Affecting or relating to cows or cattle": [
    "Bovine"
  ],
  "A shady place under trees": [
    "Bower"
  ],
  "A factory where beer is made": [
    "Brewery"
  ],
  "Member of a band of robbers": [
    "Brigand"
  ],
  "Hard but easily broken": [
    "Brittle"
  ],
  "The young of an animal cared for at one time": [
    "Brood"
  ],
  "A woman with dark brown hair": [
    "Brunette"
  ],
  "A government run by officials": [
    "Bureaucracy"
  ],
  "A hole excavated by an animal as dwelling": [
    "Burrow"
  ],
  "A group of things that have been hidden in some place": [
    "Cache"
  ],
  "One who is bad in spellings": [
    "Cacographer"
  ],
  "Harsh or discordant sound": [
    "Cacophony"
  ],
  "A person who is skilled at producing beautiful handwriting": [
    "Calligrapher"
  ],
  "The art of beautiful handwriting": [
    "Calligraphy"
  ],
  "That which makes it difficult to recognize the presence or real nature of something": [
    "Obfuscation"
  ],
  "A person who eats human flesh": [
    "Cannibal"
  ],
  "House or shelter of a gipsy": [
    "Caravan"
  ],
  "The dead body of an animal": [
    "Carcass"
  ],
  "A doctor who specializes in the study or treatment of heart diseases": [
    "Cardiologist"
  ],
  "A picture of a person or thing drawn in such an exaggerated manner as to cause laughter": [
    "Caricature"
  ],
  "A person who draws or makes maps": [
    "Cartographer"
  ],
  "The art or process of drawing or making maps": [
    "Cartography"
  ],
  "A place where gambling games are played": [
    "Casino"
  ],
  "A list or collection of books or informative graphics": [
    "Catalogue"
  ],
  "A substance that speeds up a chemical reaction without being consumed by the reaction": [
    "Catalyst"
  ],
  "Event resulting in sudden and great damage or suffering": [
    "Catastrophe"
  ],
  "Causing great damage or suffering": [
    "Catastrophic"
  ],
  "A local meeting of party members to select candidates, etc.": [
    "Caucus"
  ],
  "Soldiers who fight on horseback": [
    "Cavalry"
  ],
  "A time when enemies agree to stop fighting": [
    "Ceasefire"
  ],
  "A person who readily believes others": [
    "Credulous"
  ],
  "A person or idea that can be believed or trusted": [
    "Credible"
  ],
  "A place where a dead person’s body is cremated": [
    "Crematorium"
  ],
  "A principle or standard by which anything is or can be judged": [
    "Criterion"
  ],
  "A person who sneers at the aims and beliefs of his fellow men": [
    "Cynic"
  ],
  "The sound made by frogs": [
    "Croak"
  ],
  "The study of secret writing and coded language or words": [
    "Cryptography"
  ],
  "Guilty of the crime": [
    "Culpable"
  ],
  "Person who is the custodian of a museum or gallery": [
    "Curator"
  ],
  "A long and determined attempt to achieve something that you believe in strongly": [
    "Crusade"
  ],
  "Extreme fear of dogs": [
    "Cynophobia"
  ],
  "Center of attraction": [
    "Cynosure"
  ],
  "The branch of biology dealing with cells": [
    "Cytology"
  ],
  "A period of ten years": [
    "Decade"
  ],
  "To injure someone’s reputation by false and harmful communication": [
    "Defamation"
  ],
  "A disturbed state of mind caused by an illness, fever or intoxication": [
    "Delirium"
  ],
  "A political system in which people elect representatives to form a government": [
    "Democracy"
  ],
  "The study of population and its characteristics": [
    "Demography"
  ],
  "The branch of medicine that deals with skin diseases": [
    "Dermatology"
  ],
  "A doctor who studies and treats skin diseases": [
    "Dermatologist"
  ],
  "Skillful with the hands": [
    "Dexterous"
  ],
  "The process of finding the nature of a disease": [
    "Diagnosis"
  ],
  "A form of language peculiar to a specific region or group": [
    "Dialect"
  ],
  "A leader who wins his followers by his powerful oratory": [
    "Demagogue"
  ],
  "A ruler with total power over a country, typically one who has obtained control by force": [
    "Dictator"
  ],
  "A person who dabbles in the arts or literature without serious interest": [
    "Dilettante"
  ],
  "A person who craves for alcoholic drinks": [
    "Dipsomaniac"
  ],
  "A song sung in the past at a funeral or a lament for the dead": [
    "Dirge"
  ],
  "Government by two rulers or authorities": [
    "Diarchy"
  ],
  "A person who investigates and solves crimes": [
    "Detective"
  ],
  "A person without a home, a job or property": [
    "Derelict"
  ],
  "A file system in a computer that organizes documents and folders": [
    "Directory"
  ],
  "Angry or dissatisfied, especially due to unfair treatment": [
    "Disgruntled"
  ],
  "To break into small parts as the result of impact or decay": [
    "Disintegrate"
  ],
  "To make known private or sensitive information": [
    "Divulge"
  ],
  "A place under the control of a ruler or government": [
    "Dominion"
  ],
  "A building primarily offering sleeping accommodation to students": [
    "Dormitory"
  ],
  "To pull out or extract something": [
    "Draw"
  ],
  "Nest of a squirrel": [
    "Drey"
  ],
  "An uncontrollable urge or mania for wandering or traveling": [
    "Dromomania"
  ],
  "A place of fixed and permanent home by an individual": [
    "Domicile"
  ],
  "Capable of being bent or pulled into a shape without breaking": [
    "Ductile"
  ],
  "One who can’t speak": [
    "Dumb"
  ],
  "A range of different things": [
    "Diversity"
  ],
  "Change the appearance to deceive or to hide true identity": [
    "Disguise"
  ],
  "One who listens secretly to private conversation": [
    "Eavesdropper"
  ],
  "A person with abnormal habits or eccentricities": [
    "Eccentric"
  ],
  "Repetition of a sound caused by reflection of sound waves": [
    "Echo"
  ],
  "Study of the interaction of organisms with their environment": [
    "Ecology"
  ],
  "A thing fit to be eaten": [
    "Edible"
  ],
  "A man behaving more like a woman than a man": [
    "Effeminate"
  ],
  "Productive and achieving maximum output with minimum wasted effort or expense": [
    "Efficient"
  ],
  "A person who believes in the equality of all people": [
    "Egalitarian"
  ],
  "A person who is preoccupied with his own interests": [
    "Egoist"
  ],
  "A person who speaks always in praise of himself / excessively conceited": [
    "Egotist"
  ],
  "All the people in a country or area who are entitled to vote": [
    "Electorate"
  ],
  "A poem that expresses lament for the dead": [
    "Elegy"
  ],
  "A small mischievous fairy": [
    "Elf"
  ],
  "The art of effective speaking or public oratory skills": [
    "Elocution"
  ],
  "To run away secretly with a romantic partner": [
    "Elope"
  ],
  "An official order to stop doing business with another country": [
    "Embargo"
  ],
  "An act of misappropriation of money": [
    "Embezzlement"
  ],
  "A person who leaves his country to live in another": [
    "Emigrant"
  ],
  "The ability to understand another person’s feelings or experience": [
    "Empathy"
  ],
  "A book or set of books giving information about all areas of knowledge": [
    "Encyclopedia"
  ],
  "Regularly found in a particular place or among a particular group; native": [
    "Endemic"
  ],
  "Mysterious; difficult to understand": [
    "Enigmatic"
  ],
  "A scientist who studies insects": [
    "Entomologist"
  ],
  "The scientific study of insects and worms": [
    "Entomology"
  ],
  "Lasting for a very short time": [
    "Ephemeral"
  ],
  "Widespread outbreak of a disease affecting large populations at the same time": [
    "Epidemic"
  ],
  "A speech at the end of a book or play": [
    "Epilogue"
  ],
  "An inscription on a tombstone": [
    "Epitaph"
  ],
  "A state of perfect balance": [
    "Equilibrium"
  ],
  "The dates when days and nights are of equal length": [
    "Equinox"
  ],
  "One who accompanies somebody to protect him": [
    "Escort"
  ],
  "Something which lasts forever; having no end": [
    "Eternal"
  ],
  "Forever; endless duration": [
    "Eternity"
  ],
  "Something which lasts forever; having no end (adj.)": [
    "Eternal"
  ],
  "The scientific study of cultures, customs, and origins of human races": [
    "Ethnology"
  ],
  "The customary code of polite behaviour in society": [
    "Etiquette"
  ],
  "The study of the origin and history of words": [
    "Etymology"
  ],
  "A formal speech or piece of writing praising someone who has died": [
    "Eulogy"
  ],
  "Substitution of a mild for a very blunt expression": [
    "Euphemism"
  ],
  "Feelings of great happiness and excitement": [
    "Euphoria"
  ],
  "A person who lives outside his native country": [
    "Expatriate"
  ],
  "Bringing about gentle and painless death from incurable disease": [
    "Euthanasia"
  ],
  "A long and carefully organized journey or trip, especially for exploration": [
    "Expedition"
  ],
  "To make amends for (a sin or fault)": [
    "Expiate"
  ],
  "To remove objectionable passages from a text": [
    "Expurgate"
  ],
  "Spoken or done without preparation": [
    "Extempore"
  ],
  "Spending much more than is necessary or wise": [
    "Extravagant"
  ],
  "An outgoing, sociable person": [
    "Extrovert"
  ],
  "A short imaginary story, especially one with a moral": [
    "Fable"
  ],
  "An exact copy of handwriting or a picture produced by a machine": [
    "Facsimile"
  ],
  "Marked by excessive enthusiasm or devotion": [
    "Fanatic"
  ],
  "A pleasant situation that you imagine but is unlikely to happen": [
    "Fantasy"
  ],
  "Very attentive to and concerned about accuracy and detail": [
    "Fastidious"
  ],
  "Causing or resulting in death": [
    "Fatal"
  ],
  "The belief that events are decided by fate and cannot be controlled": [
    "Fatalism"
  ],
  "A person who believes that all events are predetermined or subject to fate": [
    "Fatalist"
  ],
  "The animals of a particular region or period": [
    "Fauna"
  ],
  "Capable of being done or carried out; practical": [
    "Feasible"
  ],
  "One who believes in giving equal opportunity to women in all fields": [
    "Feminist"
  ],
  "A group of birds of one kind": [
    "Flock"
  ],
  "To struggle helplessly or clumsily in water or mud": [
    "Flounder"
  ],
  "An unlikely piece of good luck": [
    "Fluke"
  ],
  "A person who sells and arranges cut flowers": [
    "Florist"
  ],
  "A group of ships sailing together": [
    "Fleet"
  ],
  "Capable of bending easily without breaking": [
    "Flexible"
  ],
  "The plants and vegetation of a particular region": [
    "Flora"
  ],
  "A person who attracts attention with a flashy style": [
    "Flamboyant"
  ],
  "Falsification of documents, etc.": [
    "Forgery"
  ],
  "Direct and outspoken": [
    "Forthright"
  ],
  "A period of two weeks": [
    "Fortnight"
  ],
  "An entrance hall in a building used by the public, especially a hotel or theatre": [
    "Foyer"
  ],
  "Something which gets broken easily": [
    "Fragile"
  ],
  "License granted to an individual or group to market a company's goods or services in a territory": [
    "Franchise"
  ],
  "Murder of one’s brother or sister": [
    "Fratricide"
  ],
  "An act of deceiving somebody in order to make money": [
    "Fraud"
  ],
  "A person who has escaped from captivity or is in hiding": [
    "Fugitive"
  ],
  "One who walks on ropes": [
    "Funambulist"
  ],
  "An act or remark that is calculated to gain an advantage": [
    "Gambit"
  ],
  "Talks a lot to explain something very trivial": [
    "Garrulous"
  ],
  "The art and practice of cooking and eating good food": [
    "Gastronomy"
  ],
  "Affecting or concerned with all or most people, things, etc.": [
    "General"
  ],
  "A branch of biology that studies heredity": [
    "Genetics"
  ],
  "The deliberate and systematic destruction of a racial, political, or cultural group": [
    "Genocide"
  ],
  "A person who studies the origin, history, and structure of the Earth": [
    "Geologist"
  ],
  "The study of the Earth’s physical structure, including rocks and soil": [
    "Geology"
  ],
  "The branch of medicine dealing with the health and care of older adults": [
    "Geriatrics"
  ],
  "Government by a council of old people; rule by elders": [
    "Gerontocracy"
  ],
  "A large, longstanding mass of ice that moves slowly down a mountain valley": [
    "Glacier"
  ],
  "A person who repairs broken window-glasses": [
    "Glazier"
  ],
  "A movement of part of the body to express an idea or feeling": [
    "Gesture"
  ],
  "Critical explanation or interpretation of a text, especially of scripture": [
    "Glossary"
  ],
  "One who eats too much": [
    "Glutton"
  ],
  "A person who loves good food and knows a lot about it; connoisseur of food": [
    "Gourmet"
  ],
  "Writing or drawings scribbled, scratched, or sprayed illicitly on a wall or other surface in a public place": [
    "Graffiti"
  ],
  "A building where grain is stored": [
    "Granary"
  ],
  "The study of handwriting and its connection with character": [
    "Graphology"
  ],
  "Tending to associate with others of one’s kind": [
    "Gregarious"
  ],
  "One who is easily deceived": [
    "Gullible"
  ],
  "A room filled with equipment for games and physical exercise": [
    "Gymnasium"
  ],
  "A false perception of things that do not really exist": [
    "Hallucination"
  ],
  "A very small village": [
    "Hamlet"
  ],
  "A building in which aircraft are housed": [
    "Hangar"
  ],
  "A lengthy and aggressive speech addressed to a large assembly": [
    "Harangue"
  ],
  "A transport vehicle for conveying the coffin at a funeral": [
    "Hearse"
  ],
  "One who believes gaining pleasure is the most important thing in life": [
    "Hedonist"
  ],
  "Preferring or attracted to sunlight": [
    "Heliophilous"
  ],
  "The therapeutic use of sunlight": [
    "Heliotherapy"
  ],
  "Animals that feed on plants": [
    "Herbivores"
  ],
  "A group of cattle or sheep": [
    "Herd"
  ],
  "A belief or opinion contrary to accepted doctrines": [
    "Heresy"
  ],
  "One who is against religion": [
    "Heretic"
  ],
  "Consisting of parts of different kinds; varied": [
    "Heterogeneous"
  ],
  "A geometrical figure with six sides": [
    "Hexagon"
  ],
  "To seize and divert (a vehicle) to one’s own use": [
    "Hijack"
  ],
  "Intellectually pretentious or snobbish person": [
    "Highbrow"
  ],
  "Very dramatic": [
    "Histrionic"
  ],
  "The killing of a person by another": [
    "Homicide"
  ],
  "(Things or people) of the same or similar kind or nature": [
    "Homogeneous"
  ],
  "Holding an office or position without receiving a salary": [
    "Honorary"
  ],
  "The sound of an owl": [
    "Hoot"
  ],
  "A large group of people": [
    "Horde"
  ],
  "The line where the land and sky seem to meet": [
    "Horizon"
  ],
  "The study of growing garden plants": [
    "Horticulture"
  ],
  "Friendly and welcoming to visitors": [
    "Hospitable"
  ],
  "A person who is kept captive until demands are met": [
    "Hostage"
  ],
  "A store or supply accumulated for future use": [
    "Hoard"
  ],
  "A box or cage for rabbits or small animals": [
    "Hutch"
  ],
  "Extreme fear of water": [
    "Hydrophobia"
  ],
  "A song or music in praise of God": [
    "Hymn"
  ],
  "A person who suffers from an imaginary illness / abnormally anxious about health": [
    "Hypochondriac"
  ],
  "A pretence of having virtuous character or beliefs that one does not really possess": [
    "Hypocrisy"
  ],
  "A person pretending to be someone he is not": [
    "Hypocrite"
  ],
  "One who attacks or criticizes cherished beliefs or institutions": [
    "Iconoclast"
  ],
  "A person’s peculiar habit or characteristic": [
    "Idiosyncrasy"
  ],
  "An image of a god used for worship": [
    "Idol"
  ],
  "The practice of worshipping statues as gods": [
    "Idolatry"
  ],
  "A circular house made of blocks of hard snow": [
    "Igloo"
  ],
  "An exaggerated statement not meant to be taken literally": [
    "Hyperbole"
  ],
  "Handwriting which is difficult or impossible to read": [
    "Illegible"
  ],
  "Unable to read or write": [
    "Illiterate"
  ],
  "To light up or make clear": [
    "Illuminate"
  ],
  "Pictures given in a book for the purpose of explaining things": [
    "Illustration"
  ],
  "Freedom from punishment or harm": [
    "Impunity"
  ],
  "A complicated or confusing state of affairs": [
    "Imbroglio"
  ],
  "A foreigner who settles in a country": [
    "Immigrant"
  ],
  "Matter which is against moral values": [
    "Immoral"
  ],
  "Resistant to a particular infection": [
    "Immune"
  ],
  "The policy of extending a country’s empire and influence": [
    "Imperialism"
  ],
  "Not allowing fluid to pass through; unaffected by outside opinions": [
    "Impervious"
  ],
  "A person who dishonestly pretends to be somebody else": [
    "Imposter"
  ],
  "Strong and impossible to defeat or change; that which cannot be taken by force": [
    "Impregnable"
  ],
  "Incapable of being approached": [
    "Inaccessible"
  ],
  "Incapable of speech distinctly or express oneself clearly": [
    "Inarticulate"
  ],
  "Not endowed with life; lifeless objects": [
    "Inanimate"
  ],
  "A sound that cannot be heard": [
    "Inaudible"
  ],
  "A reward or bonus offered to motivate action": [
    "Incentive"
  ],
  "Lack of civic-mindedness or of patriotism": [
    "Incivism"
  ],
  "Impossible to deny or disapprove": [
    "Incontrovertible"
  ],
  "That which cannot be corrected; beyond reform": [
    "Incorrigible"
  ],
  "That which cannot be believed": [
    "Incredible"
  ],
  "Incapable of feeling tired or exhausted": [
    "Indefatigable"
  ],
  "That which cannot be effaced; permanent": [
    "Indelible"
  ],
  "Originating or occurring naturally in the place where found": [
    "Indigenous"
  ],
  "Anger about an unfair situation or someone’s unfair behaviour": [
    "Indignation"
  ],
  "Not fit to eat": [
    "Inedible"
  ],
  "Something that cannot be avoided; certain to happen": [
    "Inevitable"
  ],
  "One who cannot make a mistake": [
    "Infallible"
  ],
  "Murder of an infant": [
    "Infanticide"
  ],
  "Not limited by number": [
    "Infinite"
  ],
  "A place in a large institution for the care of those who are ill": [
    "Infirmary"
  ],
  "Something that is difficult to understand": [
    "Incomprehensible"
  ],
  "Something that is necessary or crucial": [
    "Indispensable"
  ],
  "That cannot be expressed in words": [
    "Ineffable"
  ],
  "Someone not fit to be chosen or appointed": [
    "Ineligible"
  ],
  "Something that cannot be stopped or changed; certain to happen": [
    "Inexorable"
  ],
  "Easily set on fire; flammable": [
    "Inflammable"
  ],
  "That which cannot be satisfied": [
    "Insatiable"
  ],
  "One who is unable to pay debts": [
    "Insolvent"
  ],
  "The condition of being unable to sleep over a period of time": [
    "Insomnia"
  ],
  "The quality of being honest and having strong moral principles": [
    "Integrity"
  ],
  "Interval between two events": [
    "Interlude"
  ],
  "One who intervenes between two or more parties to settle differences": [
    "Intermediary"
  ],
  "The act of burying a dead person": [
    "Interment"
  ],
  "One who dies without a will": [
    "Intestate"
  ],
  "The examination or observation of one’s own mental and emotional processes": [
    "Introspection"
  ],
  "A quiet person more interested in their own thoughts and feelings than in socializing": [
    "Introvert"
  ],
  "A detailed list of things in a place": [
    "Inventory"
  ],
  "A person who supervises during an examination": [
    "Invigilator"
  ],
  "Refresh and revive": [
    "Invigorate"
  ],
  "That which cannot be conquered": [
    "Invincible"
  ],
  "That which cannot be called back": [
    "Irrevocable"
  ],
  "A period between reigns or governments": [
    "Interregnum"
  ],
  "A person who travels from place to place": [
    "Itinerant"
  ],
  "A plan of a journey, including the route and the places that will be visited": [
    "Itinerary"
  ],
  "Special words and phrases used by particular groups, especially in their work": [
    "Jargon"
  ],
  "A person or thing that brings bad luck": [
    "Jinx"
  ],
  "A person who rides in horse races, especially as a profession": [
    "Jockey"
  ],
  "The work of collecting and writing news, stories for newspapers, magazines, radio or television": [
    "Journalism"
  ],
  "The science or philosophy of law": [
    "Jurisprudence"
  ],
  "A group of members of the public who listen to the facts of a case in a court and decide guilt or innocence": [
    "Jury"
  ],
  "Placing different things side by side to create an interesting effect": [
    "Juxtapose"
  ],
  "Small shelter for dog": [
    "Kennel"
  ],
  "The inner soft part of a seed, fruit or nut": [
    "Kernel"
  ],
  "A recurrent urge to steal, without need or profit": [
    "Kleptomania"
  ],
  "A natural skill or aptitude": [
    "Knack"
  ],
  "The solemn sound of a funeral bell": [
    "Knell"
  ],
  "Two lengths of rope, bamboo or wood with rungs, used for climbing": [
    "Ladder"
  ],
  "A secluded or hidden retreat": [
    "Lair"
  ],
  "Property or money bequeathed by will": [
    "Legacy"
  ],
  "Pertaining to or resembling a lion": [
    "Leonine"
  ],
  "One who compiles or writes dictionaries": [
    "Lexicographer"
  ],
  "The art or practice of compiling dictionaries": [
    "Lexicography"
  ],
  "A strong band of tissues in the body that connects bones and supports organs": [
    "Ligament"
  ],
  "Feeding on mud or slime": [
    "Limivorous"
  ],
  "A person who knows several foreign languages well; one who studies languages": [
    "Linguist"
  ],
  "Easy to understand": [
    "Lucid"
  ],
  "Profitable, yielding financial gain": [
    "Lucrative"
  ],
  "A soft gentle song sung to make a child go to sleep": [
    "Lullaby"
  ],
  "Related to the moon": [
    "Lunar"
  ],
  "One who is mentally not sound": [
    "Lunatic"
  ],
  "A girl or young woman, especially an unmarried one": [
    "Maiden"
  ],
  "The first public speech delivered by a person": [
    "Maiden-speech"
  ],
  "A person who is never happy with what he has": [
    "Malcontent"
  ],
  "Any female animal which feeds its young on milk from her own body": [
    "Mammal"
  ],
  "One who talks a lot": [
    "Loquacious"
  ],
  "A large impressive house": [
    "Mansion"
  ],
  "A document written by hand before printing": [
    "Manuscript"
  ],
  "Someone who is killed for the cause of religion or faith": [
    "Martyr"
  ],
  "A person skilled in cutting, dressing, and laying stone in buildings": [
    "Mason"
  ],
  "Concerned solely with material needs; money-oriented": [
    "Materialistic"
  ],
  "A cinema show held in the afternoon": [
    "Matinee"
  ],
  "The killing of one’s mother": [
    "Matricide"
  ],
  "A stately or impressive building housing a tomb or group of tombs": [
    "Mausoleum"
  ],
  "An established principle of practical wisdom; a short statement of a general truth": [
    "Maxim"
  ],
  "An area of grassland where animals graze": [
    "Meadow"
  ],
  "To try to settle a dispute between two or more parties": [
    "Mediate"
  ],
  "A sound that is pleasing to hear": [
    "Melodious"
  ],
  "Something that serves as a reminder": [
    "Memento"
  ],
  "Of only average standard": [
    "Mediocre"
  ],
  "A person or thing that is likely to cause harm or danger": [
    "Menace"
  ],
  "Someone working or acting merely for money or other rewards; a soldier who fights for the sake of money": [
    "Mercenary"
  ],
  "Paying careful attention to every detail": [
    "Meticulous"
  ],
  "A traveller who moves from one region to another": [
    "Migrant"
  ],
  "A period of one thousand years": [
    "Millennium"
  ],
  "A place where money is coined by authority of the government": [
    "Mint"
  ],
  "A person who hates and avoids other people": [
    "Misanthrope"
  ],
  "A person who loves money and hates spending it": [
    "Miser"
  ],
  "A word or name that is inappropriate for a person or thing": [
    "Misnomer"
  ],
  "One who hates the institution of marriage": [
    "Misogamist"
  ],
  "A person who dislikes women": [
    "Misogynist"
  ],
  "One who hates reason, argument, or enlightenment": [
    "Misologist"
  ],
  "Very important or serious": [
    "Momentous"
  ],
  "A supreme ruler": [
    "Monarch"
  ],
  "A system of government by a king or queen": [
    "Monarchy"
  ],
  "A building where monks live as a community": [
    "Monastery"
  ],
  "The practice of marrying one person at a time": [
    "Monogamy"
  ],
  "Complete control of trade in particular goods or the supply of a service": [
    "Monopoly"
  ],
  "A person who believes that there is only one god": [
    "Monotheist"
  ],
  "Lacking in variety and interest; never changing and therefore boring": [
    "Monotonous"
  ],
  "A place for keeping dead bodies before burial or cremation": [
    "Mortuary"
  ],
  "A place where dead bodies are kept for identification": [
    "Morgue"
  ],
  "Commonplace; of this world rather than spiritual": [
    "Mundane"
  ],
  "A place where antiques are kept": [
    "Museum"
  ],
  "The act of refusing to obey the orders of somebody in authority, especially by soldiers/sailors": [
    "Mutiny"
  ],
  "A person or thing that has the same name as another": [
    "Namesake"
  ],
  "The habit of admiring yourself too much, especially your appearance": [
    "Narcissism"
  ],
  "A person who admires himself/herself too much, especially his appearance": [
    "Narcissist"
  ],
  "Highly unpleasant, annoying, disagreeable": [
    "Nasty"
  ],
  "Connected with the place you were born // a person, animal or plant belonging to a place by birth": [
    "Native"
  ],
  "Guide the course of a ship especially by using instruments or maps": [
    "Navigate"
  ],
  "Deserved and unavoidable punishment/ Downfall that satisfies natural justice": [
    "Nemesis"
  ],
  "A person who has recently started an activity": [
    "Neophyte"
  ],
  "A doctor who studies and treats diseases of the kidneys": [
    "Nephrologist"
  ],
  "Giving undue favors to one’s own family or friends in business or politics": [
    "Nepotism"
  ],
  "A doctor who studies and treats diseases of the nervous system": [
    "Neurologist"
  ],
  "The cry of a horse": [
    "Neigh"
  ],
  "Beginning to exist; recently formed or developed": [
    "Nascent"
  ],
  "A transcendent state in which there is neither suffering, desire, nor sense of self": [
    "Nirvana"
  ],
  "People of no fixed abode": [
    "Nomads"
  ],
  "Sentimental longing for a period in the past": [
    "Nostalgia"
  ],
  "Well-known for being bad; having an evil reputation": [
    "Notorious"
  ],
  "A person who is new to a profession without training or experience in a skill or subject": [
    "Novice"
  ],
  "The study or collection of coins": [
    "Numismatics"
  ],
  "A person who collects or studies coins": [
    "Numismatist"
  ],
  "An extreme fear of darkness": [
    "Nyctophobia"
  ],
  "A notice of a person’s death, especially in a newspaper": [
    "Obituary"
  ],
  "Something no longer in use": [
    "Obsolete"
  ],
  "Relating to the countries of the West": [
    "Occidental"
  ],
  "A geometrical figure with eight sides": [
    "Octagon"
  ],
  "One who is eighty years old": [
    "Octogenarian"
  ],
  "A person who attends to the diseases of the eye": [
    "Oculist"
  ],
  "Obsession for wine": [
    "Oenomania"
  ],
  "Government or rule by a small group of people": [
    "Oligarchy"
  ],
  "Suggesting that something unpleasant is likely to happen": [
    "Ominous"
  ],
  "One who is all-powerful": [
    "Omnipotent"
  ],
  "Present everywhere": [
    "Omnipresent"
  ],
  "One who knows everything": [
    "Omniscient"
  ],
  "An animal or person that eats a variety of food of both plant and animal origin": [
    "Omnivore"
  ],
  "One who eats both vegetables and meat": [
    "Omnivorous"
  ],
  "That through which light cannot pass": [
    "Opaque"
  ],
  "Fear of snakes": [
    "Ophiophobia"
  ],
  "A doctor who specializes in the diseases of the eyes": [
    "Ophthalmologist"
  ],
  "The study of snakes": [
    "Ophiology"
  ],
  "One who sees the bright side of things": [
    "Optimist"
  ],
  "A proficient public speaker": [
    "Orator"
  ],
  "A piece of land or garden in which fruit trees are planted": [
    "Orchard"
  ],
  "A person who studies birds": [
    "Ornithologist"
  ],
  "The scientific study of birds": [
    "Ornithology"
  ],
  "A child whose parents are dead": [
    "Orphan"
  ],
  "A public institution for the care and protection of children without parents": [
    "Orphanage"
  ],
  "Conforming to established doctrine, especially in religion": [
    "Orthodox"
  ],
  "Doctor who deals with bone problems": [
    "Orthopaedist"
  ],
  "Belief that war and violence are unjustified": [
    "Pacifism"
  ],
  "A person who opposes war or use of military force": [
    "Pacifist"
  ],
  "A formal agreement between two or more nations or peoples": [
    "Pact"
  ],
  "A doctor who treats children’s diseases": [
    "Pediatrician"
  ],
  "A solution for all difficulties or diseases": [
    "Panacea"
  ],
  "Disease that spreads over a whole country or the world": [
    "Pandemic"
  ],
  "The belief that God is in everything, including nature": [
    "Pantheism"
  ],
  "A small room in a big house, hotel, ship etc. where glasses, dishes, spoons, food etc. are kept": [
    "Pantry"
  ],
  "Story told to illustrate a moral or spiritual truth": [
    "Parable"
  ],
  "One who lives/survives on others’ or other lives": [
    "Parasite"
  ],
  "Permission given to a prisoner to leave prison before sentence ends on condition of good behaviour": [
    "Parole"
  ],
  "The crime of killing your father, mother or a close relative": [
    "Parricide"
  ],
  "One who has suddenly gained new wealth, power or prestige": [
    "Parvenu"
  ],
  "The scientific study of diseases": [
    "Pathology"
  ],
  "The study of ancient writings and scriptures": [
    "Palaeography"
  ],
  "A word that reads the same backwards as forwards": [
    "Palindrome"
  ],
  "A system of society or government in which men hold the power and women are largely excluded from it": [
    "Patriarchy"
  ],
  "Killing of one’s own father": [
    "Patricide"
  ],
  "Property that is given to somebody when his father dies": [
    "Patrimony"
  ],
  "One who loves, supports and defends his country": [
    "Patriot"
  ],
  "One who has no money or means of livelihood left": [
    "Pauper"
  ],
  "A person who insists on adherence to formal rules or literary meaning": [
    "Pedant"
  ],
  "Overly concerned with minute details or formalisms": [
    "Pedantic"
  ],
  "A structure in the garden where climbing plants can grow and people can walk under": [
    "Pergola"
  ],
  "Continuing for a long period of time without interruption; lasting forever or indefinitely": [
    "Perpetual"
  ],
  "An incidental benefit awarded for certain types of employment; an extra profit or allowance additional to a main income": [
    "Perquisite"
  ],
  "A person who walks on foot and not travelling in a vehicle": [
    "Pedestrian"
  ],
  "A strong or habitual liking for something; a tendency": [
    "Penchant"
  ],
  "Constant effort to achieve something": [
    "Perseverance"
  ],
  "A person who always expects bad things to happen": [
    "Pessimist"
  ],
  "A chemical used to kill insects or rodents": [
    "Pesticide"
  ],
  "Someone who freely gives money or help to people in need": [
    "Philanthropist"
  ],
  "Love of mankind; charitable goodwill": [
    "Philanthropy"
  ],
  "A collector or student of postage stamps": [
    "Philatelist"
  ],
  "One who dislikes or is hostile to culture and the arts": [
    "Philistine"
  ],
  "Study of language and its development": [
    "Philology"
  ],
  "Intense and unreasonable fear or dislike": [
    "Phobia"
  ],
  "Study of the sounds of human speech": [
    "Phonetics"
  ],
  "Branch of biology dealing with the function of living organisms": [
    "Physiology"
  ],
  "The act of stealing things of little value in small amounts": [
    "Pilferage"
  ],
  "One who does something for the first time; a trailblazer": [
    "Pioneer"
  ],
  "Someone who attacks and robs ships at sea": [
    "Pirate"
  ],
  "Evoking a keen sense of sadness or regret": [
    "Poignant"
  ],
  "The study or art of political governance": [
    "Politics"
  ],
  "Having more than one wife at the same time": [
    "Polygamy"
  ],
  "One who knows and uses several languages": [
    "Polyglot"
  ],
  "Practice of a woman having more than one husband": [
    "Polyandry"
  ],
  "A formal promise or undertaking": [
    "Pledge"
  ],
  "Seeming reasonable or probable": [
    "Plausible"
  ],
  "One who brings a lawsuit": [
    "Plaintiff"
  ],
  "Stealing another’s written work": [
    "Plagiarism"
  ],
  "One who steals another’s writings or ideas": [
    "Plagiarist"
  ],
  "To steal and pass off another’s work as one’s own": [
    "Plagiarise"
  ],
  "Something that can be carried easily": [
    "Portable"
  ],
  "A collection of drawings, documents, etc., representing an artist’s work": [
    "Portfolio"
  ],
  "Occurring or coming into existence after a person’s death": [
    "Posthumous"
  ],
  "A medical examination of a dead body": [
    "Postmortem"
  ],
  "A note appended to a letter after its signature": [
    "Postscript"
  ],
  "Fit to drink (water)": [
    "Potable"
  ],
  "An animal that lives by killing and eating other animals": [
    "Predator"
  ],
  "An introduction to a book explaining the author’s aims": [
    "Preface"
  ],
  "The first public performance of a theatrical work or film": [
    "Premiere"
  ],
  "A strong feeling that something is about to happen, especially something unpleasant": [
    "Premonition"
  ],
  "To make evasive or misleading statements": [
    "Prevaricate"
  ],
  "A person, especially a young one, with exceptional abilities": [
    "Prodigy"
  ],
  "An introduction to a literary work": [
    "Prologue"
  ],
  "The first design of something from which other forms are copied or developed": [
    "Prototype"
  ],
  "A feeling of deep pleasure or satisfaction derived from one’s own achievements": [
    "Pride"
  ],
  "To put off doing something, especially out of habitual carelessness or laziness": [
    "Procrastinate"
  ],
  "Spending money or resources wastefully or recklessly": [
    "Prodigal"
  ],
  "To forbid or condemn something as harmful or unlawful": [
    "Proscribe"
  ],
  "The main character in a literary work or story": [
    "Protagonist"
  ],
  "A formal set of rules or procedures governing conduct": [
    "Protocol"
  ],
  "The study of election trends by means of opinion polls": [
    "Psephologist"
  ],
  "The scientific study of voting behavior": [
    "Psephology"
  ],
  "A fictitious name especially one assumed by an author": [
    "Pseudonym"
  ],
  "The scientific study of the mind and how it influences behaviour": [
    "Psychology"
  ],
  "Careful in performing duties; showing great attention to detail": [
    "Punctilious"
  ],
  "Having a sharply strong taste or smell": [
    "Pungent"
  ],
  "A compulsion to set fire to things": [
    "Pyromania"
  ],
  "An animal with four feet": [
    "Quadruped"
  ],
  "Search for something": [
    "Quest"
  ],
  "Occurring every five years": [
    "Quinquennial"
  ],
  "Unrealistically optimistic or idealistic": [
    "Quixotic"
  ],
  "A skilled storyteller or narrator": [
    "Raconteur"
  ],
  "Medical doctor who specializes in imaging (X-rays, CT, ultrasound)": [
    "Radiologist"
  ],
  "Having a stale smell or taste": [
    "Rancid"
  ],
  "To free a prisoner on payment": [
    "Ransom"
  ],
  "A person who withdraws from the world to live in seclusion": [
    "Recluse"
  ],
  "To adjust or correct; amend": [
    "Rectify"
  ],
  "Excessive adherence to official formalities": [
    "Red-Tapism"
  ],
  "Excessively wordy or repetitive": [
    "Redundant"
  ],
  "A public vote on a particular issue": [
    "Referendum"
  ],
  "Symbols or emblems of royalty": [
    "Regalia"
  ],
  "The act of killing a king": [
    "Regicide"
  ],
  "Something belonging to or surviving from an earlier period": [
    "Relic"
  ],
  "The return of someone to his own country": [
    "Repatriation"
  ],
  "A large natural or artificial lake used as a source of water supply": [
    "Reservoir"
  ],
  "To become strong in spite of many difficulties": [
    "Resilient"
  ],
  "To give back in kind or retaliate": [
    "Retaliate"
  ],
  "A person very reserved in speech": [
    "Reticent"
  ],
  "A characteristic of one thing that is suggestive of another": [
    "Reminiscence"
  ],
  "Action of reviewing past events in one’s life": [
    "Retrospection"
  ],
  "Meaningless language with an exaggerated style intended to impress; the art of effective or persuasive speaking or writing": [
    "Rhetoric"
  ],
  "One who has fixed opinions and beliefs; hard and difficult to bend": [
    "Rigid"
  ],
  "Deliberately destroy something for military advantage": [
    "Sabotage"
  ],
  "Violation of something holy or sacred": [
    "Sacrilege"
  ],
  "The state or quality of being holy": [
    "Sanctity"
  ],
  "A place of good climate for invalids": [
    "Sanatorium"
  ],
  "One who helps a person in need": [
    "Samaritan"
  ],
  "A protected place for birds and animals": [
    "Sanctuary"
  ],
  "A sacred place": [
    "Sanctum"
  ],
  "Optimistic in an apparently difficult situation": [
    "Sanguine"
  ],
  "Full of criticism and mockery": [
    "Satire"
  ],
  "A sheath for the blade of a sword": [
    "Scabbard"
  ],
  "A person who is blamed for the wrongdoings of others": [
    "Scapegoat"
  ],
  "Someone who habitually doubts accepted beliefs": [
    "Sceptic"
  ],
  "A plan of what is to be done and when": [
    "Schedule"
  ],
  "A group of fish": [
    "School"
  ],
  "Small room where dishes are washed": [
    "Scullery"
  ],
  "The artists who make sculptures": [
    "Sculptor"
  ],
  "Government not connected with religious or spiritual matters": [
    "Secular"
  ],
  "A drug or other substance that induces sleep": [
    "Soporific"
  ],
  "An instrument for detecting an earthquake": [
    "Seismograph"
  ],
  "The scientific study of earthquakes": [
    "Seismology"
  ],
  "Making or spreading scandalous claims about someone with the intention of damaging their reputation; severely abusive writing in journals": [
    "Scurrilous"
  ],
  "Aware of and able to understand other people and their feelings": [
    "Sensitive"
  ],
  "A person between the ages of 70 and 79": [
    "Septuagenarian"
  ],
  "The occurrence and development of events by chance in a happy or beneficial way": [
    "Serendipity"
  ],
  "Repeatedly committing the same offence and typically following a characteristic, predictable behaviour pattern": [
    "Serial"
  ],
  "Rearing of silkworms for production of silk": [
    "Sericulture"
  ],
  "A close-fitting cover for the blade of a weapon or tool": [
    "Sheath"
  ],
  "A large number of fish swimming together": [
    "Shoal"
  ],
  "A figure of speech by which a thing is spoken of as being that which it only resembles": [
    "Simile"
  ],
  "Happening or being done at exactly the same time": [
    "Simultaneous"
  ],
  "An office or position requiring little or no work but giving the holder status or financial benefit": [
    "Sinecure"
  ],
  "The internal or external framework of bones in a vertebrate": [
    "Skeleton"
  ],
  "A brief or short stay at a place": [
    "Sojourn"
  ],
  "A speech made to oneself, especially when alone": [
    "Soliloquy"
  ],
  "Walking in sleep": [
    "Somnambulism"
  ],
  "Someone who walks about in sleep": [
    "Somnambulist"
  ],
  "One who talks in sleep": [
    "Somniloquist"
  ],
  "The act or habit of talking in one’s sleep": [
    "Somniloquy"
  ],
  "A fourteen-line poem": [
    "Sonnet"
  ],
  "The murder of one’s sister": [
    "Sororicide"
  ],
  "Something kept as a reminder of an event": [
    "Souvenir"
  ],
  "The scientific study of caves": [
    "Speleology"
  ],
  "One who speaks on behalf of others": [
    "Spokesman"
  ],
  "Written law of a legislative body": [
    "Statute"
  ],
  "One who loads and unloads ships": [
    "Stevedore"
  ],
  "A person who can endure pain or hardship without showing his feelings": [
    "Stoic"
  ],
  "Indifference to pleasure and pain": [
    "Stoicism"
  ],
  "A government by the military class": [
    "Stratocracy"
  ],
  "A written order to attend a court of law to give evidence": [
    "Subpoena"
  ],
  "The right to vote in political elections": [
    "Suffrage"
  ],
  "The action of killing oneself intentionally": [
    "Suicide"
  ],
  "A final performance or effort, especially before retirement or death": [
    "Swan Song"
  ],
  "A group or large number of insects or people moving together": [
    "Swarm"
  ],
  "A building where the Jews meet for religious worship and teaching": [
    "Synagogue"
  ],
  "Words of the same meanings": [
    "Synonyms"
  ],
  "Of or connected with the sense of touch": [
    "Tactile"
  ],
  "A person who preserves skin or hides of dead animals by stuffing and mounting them": [
    "Taxidermist"
  ],
  "The art of cleaning and preserving animal skins": [
    "Taxidermy"
  ],
  "A person who never takes alcoholic drinks": [
    "Teetotaller"
  ],
  "Power of reading thoughts of others": [
    "Telepathy"
  ],
  "A violent windstorm": [
    "Tempest"
  ],
  "Holding on to something or keeping an opinion with determination": [
    "Tenacious"
  ],
  "A written statement about someone’s character, usually provided by an employer": [
    "Testimonial"
  ],
  "One who believes in the existence of a god or gods": [
    "Theist"
  ],
  "Government of a country by religious leaders": [
    "Theocracy"
  ],
  "The study of the nature of God and religious beliefs": [
    "Theology"
  ],
  "A strong and fast moving stream of water": [
    "Torrent"
  ],
  "A system of government in which only one political party is allowed to function": [
    "Totalitarianism"
  ],
  "A person who works against his country": [
    "Traitor"
  ],
  "Free from disturbance; quiet and peaceful": [
    "Tranquil"
  ],
  "Lasting for only a short time (noun)": [
    "Transient"
  ],
  "That which lasts for a short time (adjective)": [
    "Transitory"
  ],
  "Allowing you to see through it (glass, etc.)": [
    "Transparent"
  ],
  "Distorted representation of something": [
    "Travesty"
  ],
  "The crime of betraying one’s country": [
    "Treason"
  ],
  "Those who pass through this gate without permission will be prosecuted (noun)": [
    "Trespassers"
  ],
  "Happening every three years": [
    "Triennial"
  ],
  "A set of three related works by the same author": [
    "Trilogy"
  ],
  "Not important or serious; obvious and dull": [
    "Trivial"
  ],
  "A student who idly or without excuse absents himself/herself from school": [
    "Truant"
  ],
  "The sound made by an elephant": [
    "Trumpet"
  ],
  "By everyone in a particular group": [
    "Unanimously"
  ],
  "Found all over the world": [
    "Universal"
  ],
  "Something never done or known before": [
    "Unprecedented"
  ],
  "Difficult to manage or handle because of size or weight": [
    "Unwieldy"
  ],
  "One who lends money on high rates of interest": [
    "Usurer"
  ],
  "An imagined society where everything is perfect and everyone is happy": [
    "Utopia"
  ],
  "Excessively fond of one’s wife": [
    "Uxorious"
  ],
  "One who switches to an opposing party": [
    "Turncoat"
  ],
  "A person who is unduly anxious about his/her health": [
    "Valetudinarian"
  ],
  "One who damages public property": [
    "Vandal"
  ],
  "Killer of a prophet": [
    "Vaticide"
  ],
  "One who eats no animal flesh": [
    "Vegetarian"
  ],
  "The speed of something in a particular direction": [
    "Velocity"
  ],
  "A slight fault that can be forgiven": [
    "Venial"
  ],
  "One who has the art of speaking in such a way that the sound seems to come from another person/place": [
    "Ventriloquist"
  ],
  "In exactly the same words as were used originally": [
    "Verbatim"
  ],
  "Someone having many skills": [
    "Versatile"
  ],
  "Evening prayer in church": [
    "Vespers"
  ],
  "A person who is long experienced or practiced in an activity": [
    "Veteran"
  ],
  "To show or state that someone or something is not guilty of something; proved to be right in court": [
    "Vindicate"
  ],
  "A person who possesses outstanding technical ability in a particular art or field": [
    "Virtuoso"
  ],
  "The cultivation of grapevines": [
    "Viticulture"
  ],
  "A substance easily evaporated at normal temperatures": [
    "Volatile"
  ],
  "Of one’s own free will": [
    "Voluntary"
  ],
  "One who offers one’s services without being forced": [
    "Volunteer"
  ],
  "A long sea journey": [
    "Voyage"
  ],
  "Exposed to the possibility of being attacked or harmed, either physically or emotionally": [
    "Vulnerable"
  ],
  "Forsaken or neglected child who has no home and spends most of his/her time on the streets": [
    "Waif"
  ],
  "A place where clothes are kept": [
    "Wardrobe"
  ],
  "A man whose wife is dead": [
    "Widower"
  ],
  "An unexpected piece of good fortune": [
    "Windfall"
  ],
  "To dispute angrily": [
    "Wrangle"
  ],
  "A decorative ring of flowers and leaves": [
    "Wreath"
  ],
  "Fear of foreigners": [
    "Xenophobia"
  ],
  "A person who is fanatical and uncompromising in pursuit of their ideals": [
    "Zealot"
  ]
}

def swap_key_value(data):
    """Swaps the keys and values of the input dictionary."""
    swapped_data = {}
    for key, value_list in data.items():
        if isinstance(value_list, list):
            for value in value_list:
                swapped_data[value.strip()] = [key.strip()]
    return swapped_data

def generate_all_questions(data_source):
    """
    Generates a complete list of questions from a given data source.
    
    Args:
        data_source (dict): The dictionary (e.g., PREPOSITIONS_DATA) to use.

    Returns:
        list: A list of question dictionaries.
    """
    if not data_source:
        return []

    # this was removed as it was creating some issues with common answer questions
    # swapped_data = swap_key_value(data_source)
    swapped_data = data_source
    data_entries = list(swapped_data.items())
    all_answers = [item[1][0] for item in data_entries]
    
    questions = []
    
    for i, (phrase, definitions) in enumerate(data_entries):
        correct_answer = definitions[0]
        
        # Get 3 unique wrong options
        wrong_options = set()
        while len(wrong_options) < 3 and len(wrong_options) < len(all_answers) - 1:
            random_choice = random.choice(all_answers)
            if random_choice != correct_answer:
                wrong_options.add(random_choice)
        
        # Combine options and shuffle
        options = list(wrong_options) + [correct_answer]
        random.shuffle(options)
        
        questions.append({
            "numb": i + 1,
            "question": f'"{phrase}"',
            "answer": correct_answer,
            "options": options
        })
        
    return questions
