# muss noch angepasst werden !! (Vokabeln und Parteien)

from collections import Counter

# File output: Wordcounts.csv with counts for individual MFD words for both labour and conservative
writefile = open('wordcounts.csv','w')
labour = open('labourTweets_InclusionCriteriaMet_CLEANED.txt').read()
conservative = open('conservativeTweets_InclusionCriteriaMet_CLEANED.txt').read()

# lists containing all the words included in MFD categories. a space after a word indicates a word, no space means its a word stem. e.g. sympath will pick up sympathy/sympathetic
harmcare = [' safe',' peace',' compassion',' empath',' sympath',' care ',' caring ',' protect',' shield ',' shelter ',' amity ',' secur',' benefit',' defen',' guard',' preserve ',' harm',' suffer',' war ',' wars ',' warl',' warring ',' fight',' violen',' hurt',' kill ',' kills ',' killer',' killed ',' killing ',' endanger',' cruel',' brutal',' abuse',' damag',' ruin',' ravage ',' detriment',' crush',' attack',' annihalate',' destroy ',' stomp ',' abandon',' spurn ',' impair ',' exploit ',' exploits ',' exploited ',' exploting ',' wound']
fairness = [' fair ',' fairly ',' fairness ',' fair-',' fairmind',' fairplay',' equal',' justice ', ' justness ', ' justifi', ' reciproc',' impartial', ' egalitar',' rights ', ' equity ',' evenness ', ' equivalent ', ' unbias', ' tolerant ', ' equable ', ' balance', ' homologous ',' unprejudice', ' reasonable ', ' constant ', ' honest', ' unfair',' unequal', ' bias',' unjust', ' injust',' bigot', ' discriminat', ' disproportion',' inequitable ', ' prejud', ' dishonest ', ' unscrupulous ', ' dissociate ', ' preference ',' favoritism ', ' segregat',' exclusion ', ' exclud']
ingroup = [' segregat',' abandon',' together ', ' nation' , ' homeland' , ' family ', ' families ', ' familial ', ' group ', ' loyal' , ' patriot' , ' communal ', ' commune' , ' communit' , ' communis' , ' comrad' , ' cadre ', ' collectiv' , ' joint ', ' unison ', ' unite' , ' fellow' , ' guild ', ' solidarity ', ' devot' , ' member ', ' cliqu' , ' cohort ', ' ally ', ' insider ', ' foreign' , ' enem' , ' betray' , ' treason' , ' traitor' , ' treacher' , ' disloyal' , ' individual' , ' apostasy ', ' apostate ', ' deserted ', ' deserter' , ' deserting ', ' deceiv' , ' jilt' , ' imposter ', ' miscreant ', ' spy ', ' sequester ', ' renegade ', ' terroris' , ' immigra']
authority = [' preserve ',' betray',' treason',' traitor',' treacher',' disloyal',' individual',' apostasy ',' apostate ',' deserted ',' deserter', ' deserting ',' loyal',' preserve',' obey' , ' obedien' , ' duty ', ' law ', ' lawful' , ' legal' , ' duti' , ' honor' , ' respect ',' respectful',' respected ',' respects ', ' order' , ' father' , ' mother ',' motherl',' mothering ',' mothers ', ' tradition' , ' hierarch' , ' authorit' , ' permit ', ' permission ', ' status' , ' rank' , ' leader' , ' class ', ' bourgeoisie ', ' caste' , ' position ', ' complian' , ' command ', ' supremacy ', ' control ', ' submi' , ' allegian' , ' serve ', ' abide ', ' defere', ' defer ', ' revere', ' venerat' , ' comply ', ' defian' , ' rebel' , ' dissent' , ' subver' , ' disrespect' , ' disobe' , ' sediti' , ' agitat' , ' insubordinat' , ' illegal' , ' lawless' , ' insurgent ', ' mutinous ', ' defy' , ' dissident ', ' unfaithful ', ' alienate ', ' defector ', ' heretic'  , ' nonconformist ', ' oppose ', ' protest ', ' refuse ', ' denounce ', ' remonstrate ', ' riot' , ' obstruct ']
purity = [' loyal',' heretic',' apostasy',' apostate',' exploit ',' exploits ',' exploited ',' exploting ',' ruin',' preserve',' piety ', ' pious ', ' purity ', ' pure' , ' clean' , ' steril' , ' sacred' , ' chast' , ' holy ', ' holiness ', ' saint' , ' wholesome' , ' celiba' , ' abstention ', ' virgin ',' virgins ',' virginity ',' virginal ', ' austerity ', ' integrity ', ' modesty ', ' abstinen' , ' abstemiousness', ' upright ', ' limpid ', ' unadulterated ', ' maiden ', ' virtuous ', ' refined ', ' decen' , ' immaculate ', ' innocent ', ' pristine ', ' church', ' disgust' , ' deprav' , ' disease' , ' unclean' , ' contagio' , ' indecen', ' sin ',' sinful',' sinner',' sins ',' sinned ',' sinning ',  ' slut' , ' whore ', ' dirt', ' impiety ', ' impious ', ' profan' , ' gross ', ' repuls' , ' sick' , ' promiscu' , ' lewd', ' adulter' , ' debauche' , ' defile' , ' tramp ', ' prostitut' , ' unchaste ', ' wanton ', ' profligate ', ' filth' , ' trashy ', ' obscen' , ' lax ', ' taint' , ' stain' , ' tarnish' , ' debase' , ' desecrat' , ' wicked' , ' blemish ', ' exploitat' , ' pervert ', ' wretched']
liberty = [' authorit',' lawful',' legal',' unfair',' unjust',' injust',' discriminat',' prejud',' segregat',' freedom ', ' choice ', ' emancipat', ' liberty ', ' autonom', ' independen', ' right', ' opportunity ', ' free ', ' equal', ' democra', ' constitution ', ' amnesty ', ' civil ', ' individual', ' mobility ', ' movement ', ' resist', ' empower', ' oppress', ' sanction', ' prohibit', ' enforce ', ' arrest', ' imprison', ' silence ', ' tyran', ' depriv', ' infringe ', ' restrain', ' slave', ' dictator', ' intoleran', ' violat', ' prison', ' jail', ' censor', ' border ', ' exploit', ' tariff', ' authoritarian ', ' punitive ', ' punish', ' brutal', ' persecut', ' repress' ]

def wordcounts(foundation):
    labourcare = []
    conservativecare = []
    for word in foundation:
        countcarelabour = labour.count(word)
        countcareconservative = conservative.count(word)
        labourcare.append(countcarelabour)
        conservativecare.append(countcareconservative)
        writefile.write(str(word)+str(', ') +str(countcarelabour)+str(', ') +str(countcareconservative)+'\n')

wordcounts(harmcare)
wordcounts(fairness)
wordcounts(ingroup)
wordcounts(authority)
wordcounts(purity)
wordcounts(liberty)
