## UbSecEmergencyResponseTools ##
```
 hacker /EmergencyResponseTools/Linux/Ubsec 
➜  python UbSec.py                                                ✔  15:11:56

 _    _           _                      _   _    _____
| |  | |         | |                    | | | |  / ____|
| |  | |_ __ ___ | |__  _ __ ___  __ _  | | | | | (___   ___  ___
| |  | | '_ ` _ \| '_ \| '__/ _ \/ _` | | | | |  \___ \ / _ \/ __|
| |__| | | | | | | |_) | | |  __/ (_| | | | | |  ____) |  __/ (__
 \____/|_| |_| |_|_.__/|_|  \___|\__,_| |_| |_| |_____/ \___|\___|



	 {version:v0.1}
	 {author:圣诞}
```
自用工具，不喜勿喷。。。
```
➜  tree                                                           ✔  15:36:27
.
├── README.md
├── UbSec.py
├── db
│   └── hash_db.txt
├── lib
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── core
│   │   ├── Traceability.py
│   │   ├── Traceability.pyc
│   │   ├── __init__.py
│   │   ├── __init__.pyc
│   │   ├── common.py
│   │   ├── common.pyc
│   │   ├── globalvar.py
│   │   ├── globalvar.pyc
│   │   ├── ip
│   │   │   ├── 17monipdb.dat
│   │   │   ├── __init__.py
│   │   │   ├── __init__.pyc
│   │   │   ├── ip.py
│   │   │   └── ip.pyc
│   │   ├── option.py
│   │   └── option.pyc
│   ├── egg
│   │   ├── yara_python-3.5.0-py2.6-linux-2.32-x86_64.egg
│   │   │   ├── EGG-INFO
│   │   │   │   ├── PKG-INFO
│   │   │   │   ├── SOURCES.txt
│   │   │   │   ├── dependency_links.txt
│   │   │   │   ├── native_libs.txt
│   │   │   │   ├── not-zip-safe
│   │   │   │   └── top_level.txt
│   │   │   ├── yara.py
│   │   │   ├── yara.pyc
│   │   │   └── yara.so
│   │   ├── yara_python-3.5.0-py2.7-linux-3.10-x86_64.egg
│   │   │   ├── EGG-INFO
│   │   │   │   ├── PKG-INFO
│   │   │   │   ├── SOURCES.txt
│   │   │   │   ├── dependency_links.txt
│   │   │   │   ├── native_libs.txt
│   │   │   │   ├── not-zip-safe
│   │   │   │   └── top_level.txt
│   │   │   ├── yara.py
│   │   │   ├── yara.pyc
│   │   │   └── yara.so
│   │   ├── yara_python-3.5.0-py2.7-macosx-10.12-x86_64.egg
│   │   │   ├── EGG-INFO
│   │   │   │   ├── PKG-INFO
│   │   │   │   ├── SOURCES.txt
│   │   │   │   ├── dependency_links.txt
│   │   │   │   ├── native_libs.txt
│   │   │   │   ├── not-zip-safe
│   │   │   │   └── top_level.txt
│   │   │   ├── yara.py
│   │   │   ├── yara.pyc
│   │   │   └── yara.so
│   │   ├── yara_python-3.5.0-py2.7-macosx-10.13-x86_64.egg
│   │   │   ├── EGG-INFO
│   │   │   │   ├── PKG-INFO
│   │   │   │   ├── SOURCES.txt
│   │   │   │   ├── dependency_links.txt
│   │   │   │   ├── installed-files.txt
│   │   │   │   ├── not-zip-safe
│   │   │   │   └── top_level.txt
│   │   │   ├── yara.py
│   │   │   ├── yara.pyc
│   │   │   └── yara.so
│   │   └── yara_python-3.8.1-py2.7-linux-4.20-x86_64.egg
│   │       ├── EGG-INFO
│   │       │   ├── PKG-INFO
│   │       │   ├── SOURCES.txt
│   │       │   ├── dependency_links.txt
│   │       │   ├── native_libs.txt
│   │       │   ├── not-zip-safe
│   │       │   └── top_level.txt
│   │       ├── yara.py
│   │       └── yara.so
│   ├── malware
│   │   ├── 9002.txt
│   │   ├── aboc.txt
│   │   ├── acridrain.txt
│   │   ├── activeagent.txt
│   │   ├── advisorbot.txt
│   │   ├── adylkuzz.txt
│   │   ├── adzok.txt
│   │   ├── agaadex.txt
│   │   ├── agenttesla.txt
│   │   ├── alienspy.txt
│   │   ├── alina.txt
│   │   ├── almalocker.txt
│   │   ├── alureon.txt
│   │   ├── amadey.txt
│   │   ├── ammyyrat.txt
│   │   ├── android_acecard.txt
│   │   ├── android_adrd.txt
│   │   ├── android_alienspy.txt
│   │   ├── android_anubis.txt
│   │   ├── android_arspam.txt
│   │   ├── android_asacub.txt
│   │   ├── android_backflash.txt
│   │   ├── android_bankbot.txt
│   │   ├── android_bankinfostealer.txt
│   │   ├── android_bankun.txt
│   │   ├── android_basbanke.txt
│   │   ├── android_basebridge.txt
│   │   ├── android_besyria.txt
│   │   ├── android_boxer.txt
│   │   ├── android_buhsam.txt
│   │   ├── android_busygasper.txt
│   │   ├── android_chuli.txt
│   │   ├── android_claco.txt
│   │   ├── android_clickfraud.txt
│   │   ├── android_coolreaper.txt
│   │   ├── android_counterclank.txt
│   │   ├── android_cyberwurx.txt
│   │   ├── android_dendoroid.txt
│   │   ├── android_dougalek.txt
│   │   ├── android_droidjack.txt
│   │   ├── android_droidkungfu.txt
│   │   ├── android_enesoluty.txt
│   │   ├── android_ewalls.txt
│   │   ├── android_ewind.txt
│   │   ├── android_exodus.txt
│   │   ├── android_exprespam.txt
│   │   ├── android_fakeapp.txt
│   │   ├── android_fakebanco.txt
│   │   ├── android_fakedown.txt
│   │   ├── android_fakeinst.txt
│   │   ├── android_fakelog.txt
│   │   ├── android_fakemart.txt
│   │   ├── android_fakemrat.txt
│   │   ├── android_fakeneflic.txt
│   │   ├── android_fakesecsuit.txt
│   │   ├── android_feabme.txt
│   │   ├── android_flexispy.txt
│   │   ├── android_fraudbot.txt
│   │   ├── android_frogonal.txt
│   │   ├── android_geinimi.txt
│   │   ├── android_generic.txt
│   │   ├── android_ghostpush.txt
│   │   ├── android_ginmaster.txt
│   │   ├── android_gmaster.txt
│   │   ├── android_godwon.txt
│   │   ├── android_golddream.txt
│   │   ├── android_goldencup.txt
│   │   ├── android_gonesixty.txt
│   │   ├── android_gplayed.txt
│   │   ├── android_gustuff.txt
│   │   ├── android_henbox.txt
│   │   ├── android_ibanking.txt
│   │   ├── android_infostealer.txt
│   │   ├── android_jsmshider.txt
│   │   ├── android_kbuster.txt
│   │   ├── android_kemoge.txt
│   │   ├── android_lockdroid.txt
│   │   ├── android_lotoor.txt
│   │   ├── android_lovetrap.txt
│   │   ├── android_maistealer.txt
│   │   ├── android_maxit.txt
│   │   ├── android_mobstspy.txt
│   │   ├── android_oneclickfraud.txt
│   │   ├── android_opfake.txt
│   │   ├── android_ozotshielder.txt
│   │   ├── android_pikspam.txt
│   │   ├── android_pjapps.txt
│   │   ├── android_qdplugin.txt
│   │   ├── android_redalert.txt
│   │   ├── android_remotecode.txt
│   │   ├── android_repane.txt
│   │   ├── android_roamingmantis.txt
│   │   ├── android_roidsec.txt
│   │   ├── android_rotexy.txt
│   │   ├── android_samsapo.txt
│   │   ├── android_sandorat.txt
│   │   ├── android_selfmite.txt
│   │   ├── android_simbad.txt
│   │   ├── android_simplocker.txt
│   │   ├── android_skullkey.txt
│   │   ├── android_sndapps.txt
│   │   ├── android_spytekcell.txt
│   │   ├── android_stealer.txt
│   │   ├── android_stels.txt
│   │   ├── android_swanalitics.txt
│   │   ├── android_teelog.txt
│   │   ├── android_tetus.txt
│   │   ├── android_tonclank.txt
│   │   ├── android_torec.txt
│   │   ├── android_triada.txt
│   │   ├── android_uracto.txt
│   │   ├── android_usbcleaver.txt
│   │   ├── android_walkinwat.txt
│   │   ├── android_windseeker.txt
│   │   ├── android_wirex.txt
│   │   ├── android_xavirad.txt
│   │   ├── android_zertsecurity.txt
│   │   ├── android_ztorg.txt
│   │   ├── androm.txt
│   │   ├── angler.txt
│   │   ├── anubis.txt
│   │   ├── anuna.txt
│   │   ├── apt_33.txt
│   │   ├── apt_38.txt
│   │   ├── apt_adwind.txt
│   │   ├── apt_aridviper.txt
│   │   ├── apt_babar.txt
│   │   ├── apt_bahamut.txt
│   │   ├── apt_barium.txt
│   │   ├── apt_bisonal.txt
│   │   ├── apt_bitter.txt
│   │   ├── apt_blackenergy.txt
│   │   ├── apt_blacktech.txt
│   │   ├── apt_blindeagle.txt
│   │   ├── apt_bookworm.txt
│   │   ├── apt_buhtrap.txt
│   │   ├── apt_c23.txt
│   │   ├── apt_careto.txt
│   │   ├── apt_casper.txt
│   │   ├── apt_cdt.txt
│   │   ├── apt_chafer.txt
│   │   ├── apt_charmingkitten.txt
│   │   ├── apt_cleaver.txt
│   │   ├── apt_cobaltdickens.txt
│   │   ├── apt_commentcrew.txt
│   │   ├── apt_copykittens.txt
│   │   ├── apt_cosmicduke.txt
│   │   ├── apt_cyberbit.txt
│   │   ├── apt_darkhotel.txt
│   │   ├── apt_darkhydrus.txt
│   │   ├── apt_deeppanda.txt
│   │   ├── apt_desertfalcon.txt
│   │   ├── apt_dnspionage.txt
│   │   ├── apt_docless.txt
│   │   ├── apt_domestickitten.txt
│   │   ├── apt_donot.txt
│   │   ├── apt_dragonok.txt
│   │   ├── apt_duke.txt
│   │   ├── apt_dustsquad.txt
│   │   ├── apt_equationgroup.txt
│   │   ├── apt_evapiks.txt
│   │   ├── apt_ezq.txt
│   │   ├── apt_familiarfeeling.txt
│   │   ├── apt_finfisher.txt
│   │   ├── apt_fruityarmor.txt
│   │   ├── apt_gallmaker.txt
│   │   ├── apt_gamaredon.txt
│   │   ├── apt_gaza.txt
│   │   ├── apt_glasses.txt
│   │   ├── apt_goblinpanda.txt
│   │   ├── apt_goldenbird.txt
│   │   ├── apt_goldenrat.txt
│   │   ├── apt_goldmouse.txt
│   │   ├── apt_gothicpanda.txt
│   │   ├── apt_gravityrat.txt
│   │   ├── apt_gref.txt
│   │   ├── apt_greyenergy.txt
│   │   ├── apt_groundbait.txt
│   │   ├── apt_group123.txt
│   │   ├── apt_group5.txt
│   │   ├── apt_hackingteam.txt
│   │   ├── apt_hogfish.txt
│   │   ├── apt_icefog.txt
│   │   ├── apt_innaput.txt
│   │   ├── apt_irn2.txt
│   │   ├── apt_irontiger.txt
│   │   ├── apt_ke3chang.txt
│   │   ├── apt_keyboy.txt
│   │   ├── apt_kimsuky.txt
│   │   ├── apt_lazarus.txt
│   │   ├── apt_leafminer.txt
│   │   ├── apt_lotusblossom.txt
│   │   ├── apt_luckymouse.txt
│   │   ├── apt_magichound.txt
│   │   ├── apt_menupass.txt
│   │   ├── apt_miniduke.txt
│   │   ├── apt_mudcarp.txt
│   │   ├── apt_muddywater.txt
│   │   ├── apt_naikon.txt
│   │   ├── apt_nettraveler.txt
│   │   ├── apt_newsbeef.txt
│   │   ├── apt_oceanlotus.txt
│   │   ├── apt_oilrig.txt
│   │   ├── apt_packrat.txt
│   │   ├── apt_patchwork.txt
│   │   ├── apt_pegasus.txt
│   │   ├── apt_potao.txt
│   │   ├── apt_quasar.txt
│   │   ├── apt_reaper.txt
│   │   ├── apt_redbaldknight.txt
│   │   ├── apt_redoctober.txt
│   │   ├── apt_rnexus.txt
│   │   ├── apt_rocketman.txt
│   │   ├── apt_sauron.txt
│   │   ├── apt_scanbox.txt
│   │   ├── apt_scarletmimic.txt
│   │   ├── apt_scieron.txt
│   │   ├── apt_sectora05.txt
│   │   ├── apt_shamoon.txt
│   │   ├── apt_sidewinder.txt
│   │   ├── apt_simbaa.txt
│   │   ├── apt_snowman.txt
│   │   ├── apt_sobaken.txt
│   │   ├── apt_sofacy.txt
│   │   ├── apt_stealthfalcon.txt
│   │   ├── apt_stolenpencil.txt
│   │   ├── apt_stonedrill.txt
│   │   ├── apt_stuxnet.txt
│   │   ├── apt_tajmahal.txt
│   │   ├── apt_telebots.txt
│   │   ├── apt_tempperiscope.txt
│   │   ├── apt_temptingcedar.txt
│   │   ├── apt_tibet.txt
│   │   ├── apt_tick.txt
│   │   ├── apt_turla.txt
│   │   ├── apt_tvrms.txt
│   │   ├── apt_unclassified.txt
│   │   ├── apt_volatilecedar.txt
│   │   ├── apt_weakestlink.txt
│   │   ├── apt_webky.txt
│   │   ├── apt_whitecompany.txt
│   │   ├── apt_wickedpanda.txt
│   │   ├── apt_windshift.txt
│   │   ├── apt_wirte.txt
│   │   ├── arcane.txt
│   │   ├── arec.txt
│   │   ├── arkei.txt
│   │   ├── artro.txt
│   │   ├── athenagorat.txt
│   │   ├── aurora.txt
│   │   ├── autoit.txt
│   │   ├── avalanche.txt
│   │   ├── avemaria.txt
│   │   ├── avrecon.txt
│   │   ├── axpergle.txt
│   │   ├── azorult.txt
│   │   ├── bachosens.txt
│   │   ├── badblock.txt
│   │   ├── balamid.txt
│   │   ├── baldr.txt
│   │   ├── bamital.txt
│   │   ├── bankapol.txt
│   │   ├── bankerflux.txt
│   │   ├── bankpatch.txt
│   │   ├── banload.txt
│   │   ├── banprox.txt
│   │   ├── bayrob.txt
│   │   ├── beapy.txt
│   │   ├── bebloh.txt
│   │   ├── bedep.txt
│   │   ├── belonard.txt
│   │   ├── biskvit.txt
│   │   ├── bizzana.txt
│   │   ├── blackshades.txt
│   │   ├── blackworm.txt
│   │   ├── blockbuster.txt
│   │   ├── bluebot.txt
│   │   ├── bobax.txt
│   │   ├── bondat.txt
│   │   ├── bot_mikrotik.txt
│   │   ├── bozokrat.txt
│   │   ├── bredolab.txt
│   │   ├── breut.txt
│   │   ├── brushaloader.txt
│   │   ├── bubnix.txt
│   │   ├── bucriv.txt
│   │   ├── bunitu.txt
│   │   ├── buterat.txt
│   │   ├── calfbot.txt
│   │   ├── camerashy.txt
│   │   ├── capturatela.txt
│   │   ├── carberp.txt
│   │   ├── cardinalrat.txt
│   │   ├── ccleaner_backdoor.txt
│   │   ├── ceidpagelock.txt
│   │   ├── cerber.txt
│   │   ├── chainshot.txt
│   │   ├── chalubo.txt
│   │   ├── changeup.txt
│   │   ├── chanitor.txt
│   │   ├── chasebot.txt
│   │   ├── cheshire.txt
│   │   ├── chewbacca.txt
│   │   ├── chisbur.txt
│   │   ├── chthonic.txt
│   │   ├── cirenegrat.txt
│   │   ├── citadel.txt
│   │   ├── cloudatlas.txt
│   │   ├── cobalt.txt
│   │   ├── conficker.txt
│   │   ├── contopee.txt
│   │   ├── corebot.txt
│   │   ├── couponarific.txt
│   │   ├── criakl.txt
│   │   ├── cridex.txt
│   │   ├── crilock.txt
│   │   ├── cryakl.txt
│   │   ├── cryptinfinite.txt
│   │   ├── cryptodefense.txt
│   │   ├── cryptolocker.txt
│   │   ├── cryptowall.txt
│   │   ├── cryptxxx.txt
│   │   ├── ctblocker.txt
│   │   ├── cutwail.txt
│   │   ├── cybergaterat.txt
│   │   ├── damoclis.txt
│   │   ├── danabot.txt
│   │   ├── dangerous.txt
│   │   ├── darkcloud.txt
│   │   ├── darkgate.txt
│   │   ├── defru.txt
│   │   ├── destory.txt
│   │   ├── dexter.txt
│   │   ├── diamondfoxrat.txt
│   │   ├── dimnie.txt
│   │   ├── dinihou.txt
│   │   ├── dircrypt.txt
│   │   ├── dmalocker.txt
│   │   ├── dmsniff.txt
│   │   ├── dnsbirthday.txt
│   │   ├── dnschanger.txt
│   │   ├── dnstrojan.txt
│   │   ├── dofoil.txt
│   │   ├── dorifel.txt
│   │   ├── dorkbot.txt
│   │   ├── dorv.txt
│   │   ├── drapion.txt
│   │   ├── dreambot.txt
│   │   ├── dridex.txt
│   │   ├── dropnak.txt
│   │   ├── dursg.txt
│   │   ├── dyreza.txt
│   │   ├── ek_nuclear.txt
│   │   ├── elf_aidra.txt
│   │   ├── elf_amnesiark.txt
│   │   ├── elf_billgates.txt
│   │   ├── elf_chalubo.txt
│   │   ├── elf_coinminer.txt
│   │   ├── elf_darlloz.txt
│   │   ├── elf_ddosman.txt
│   │   ├── elf_dofloo.txt
│   │   ├── elf_ekoms.txt
│   │   ├── elf_fbot.txt
│   │   ├── elf_gafgyt.txt
│   │   ├── elf_generic.txt
│   │   ├── elf_groundhog.txt
│   │   ├── elf_hacked_mint.txt
│   │   ├── elf_hellobot.txt
│   │   ├── elf_httpsd.txt
│   │   ├── elf_iotreaper.txt
│   │   ├── elf_mayhem.txt
│   │   ├── elf_mirai.txt
│   │   ├── elf_mokes.txt
│   │   ├── elf_mumblehard.txt
│   │   ├── elf_openssh_backdoorkit.txt
│   │   ├── elf_pasteminer.txt
│   │   ├── elf_pinscan.txt
│   │   ├── elf_rekoobe.txt
│   │   ├── elf_routex.txt
│   │   ├── elf_shelldos.txt
│   │   ├── elf_slexec.txt
│   │   ├── elf_sshscan.txt
│   │   ├── elf_themoon.txt
│   │   ├── elf_torii.txt
│   │   ├── elf_turla.txt
│   │   ├── elf_xbash.txt
│   │   ├── elf_xnote.txt
│   │   ├── elf_xorddos.txt
│   │   ├── elpman.txt
│   │   ├── emogen.txt
│   │   ├── emotet.txt
│   │   ├── evilbunny.txt
│   │   ├── evilgrab.txt
│   │   ├── evilnum.txt
│   │   ├── expiro.txt
│   │   ├── fakben.txt
│   │   ├── fakeav.txt
│   │   ├── fakeran.txt
│   │   ├── fantom.txt
│   │   ├── fareit.txt
│   │   ├── farseer.txt
│   │   ├── fbi_ransomware.txt
│   │   ├── fiexp.txt
│   │   ├── fignotok.txt
│   │   ├── filespider.txt
│   │   ├── fin4.txt
│   │   ├── fin6.txt
│   │   ├── fin7.txt
│   │   ├── findpos.txt
│   │   ├── fireball.txt
│   │   ├── fnumbot.txt
│   │   ├── fobber.txt
│   │   ├── formbook.txt
│   │   ├── forshare.txt
│   │   ├── fox.txt
│   │   ├── fraudload.txt
│   │   ├── fruitfly.txt
│   │   ├── fudcrypt.txt
│   │   ├── fynloski.txt
│   │   ├── fysna.txt
│   │   ├── gamapos.txt
│   │   ├── gamarue.txt
│   │   ├── gandcrab.txt
│   │   ├── gauss.txt
│   │   ├── gbot.txt
│   │   ├── generic.txt
│   │   ├── gh0strat.txt
│   │   ├── glitchpos.txt
│   │   ├── globeimposter.txt
│   │   ├── glupteba.txt
│   │   ├── godzilla.txt
│   │   ├── golroted.txt
│   │   ├── gootkit.txt
│   │   ├── gozi.txt
│   │   ├── gtbot.txt
│   │   ├── guildma.txt
│   │   ├── hacking_team.txt
│   │   ├── harnig.txt
│   │   ├── hawkeye.txt
│   │   ├── helompy.txt
│   │   ├── hiddenbeer.txt
│   │   ├── hiddentear.txt
│   │   ├── hiloti.txt
│   │   ├── hinired.txt
│   │   ├── hoplight.txt
│   │   ├── houdini.txt
│   │   ├── huntpos.txt
│   │   ├── icedid.txt
│   │   ├── imminentrat.txt
│   │   ├── immortal.txt
│   │   ├── infinityrat.txt
│   │   ├── injecto.txt
│   │   ├── investimer.txt
│   │   ├── invisimole.txt
│   │   ├── ios_keyraider.txt
│   │   ├── ios_muda.txt
│   │   ├── ios_oneclickfraud.txt
│   │   ├── ios_realtimespy.txt
│   │   ├── ios_specter.txt
│   │   ├── ios_xcodeghost.txt
│   │   ├── iron.txt
│   │   ├── ismdoor.txt
│   │   ├── jackpos.txt
│   │   ├── jasperloader.txt
│   │   ├── jrat.txt
│   │   ├── jripbot.txt
│   │   ├── karkoff.txt
│   │   ├── kasidet.txt
│   │   ├── kazy.txt
│   │   ├── kegotip.txt
│   │   ├── khrat.txt
│   │   ├── killrabbit.txt
│   │   ├── kingminer.txt
│   │   ├── kingslayer.txt
│   │   ├── kolab.txt
│   │   ├── konni.txt
│   │   ├── koobface.txt
│   │   ├── korgo.txt
│   │   ├── korplug.txt
│   │   ├── kovter.txt
│   │   ├── kpot.txt
│   │   ├── kradellsh.txt
│   │   ├── kromagent.txt
│   │   ├── kronos.txt
│   │   ├── kulekmoko.txt
│   │   ├── latentbot.txt
│   │   ├── limerat.txt
│   │   ├── litehttp.txt
│   │   ├── loadpcbanker.txt
│   │   ├── locked_ransomware.txt
│   │   ├── locky.txt
│   │   ├── loda.txt
│   │   ├── lokibot.txt
│   │   ├── lollipop.txt
│   │   ├── luckycat.txt
│   │   ├── luoxk.txt
│   │   ├── magentocore.txt
│   │   ├── magicpos.txt
│   │   ├── magniber.txt
│   │   ├── majikpos.txt
│   │   ├── malwaremustdie.org.txt
│   │   ├── mambashim.txt
│   │   ├── marap.txt
│   │   ├── marsjoke.txt
│   │   ├── matrix.txt
│   │   ├── matsnu.txt
│   │   ├── mdrop.txt
│   │   ├── mebroot.txt
│   │   ├── megaopac.txt
│   │   ├── mestep.txt
│   │   ├── metamorfo.txt
│   │   ├── minotaur.txt
│   │   ├── misogow.txt
│   │   ├── miuref.txt
│   │   ├── modpos.txt
│   │   ├── moreeggs.txt
│   │   ├── morto.txt
│   │   ├── mysticalnet.txt
│   │   ├── nampohyu.txt
│   │   ├── nanocore.txt
│   │   ├── nbot.txt
│   │   ├── necurs.txt
│   │   ├── nekostealer.txt
│   │   ├── nemeot.txt
│   │   ├── neonwallet.txt
│   │   ├── neshuta.txt
│   │   ├── netsupport.txt
│   │   ├── netwire.txt
│   │   ├── neurevt.txt
│   │   ├── nexlogger.txt
│   │   ├── ngioweb.txt
│   │   ├── nigelthorn.txt
│   │   ├── nitol.txt
│   │   ├── nivdort.txt
│   │   ├── njrat.txt
│   │   ├── nonbolqu.txt
│   │   ├── notpetya.txt
│   │   ├── novelminer.txt
│   │   ├── novobot.txt
│   │   ├── nozelesn.txt
│   │   ├── nucleartor.txt
│   │   ├── nuqel.txt
│   │   ├── nwt.txt
│   │   ├── nymaim.txt
│   │   ├── nymeria.txt
│   │   ├── odcodc.txt
│   │   ├── oficla.txt
│   │   ├── onkods.txt
│   │   ├── optima.txt
│   │   ├── osx_generic.txt
│   │   ├── osx_keranger.txt
│   │   ├── osx_keydnap.txt
│   │   ├── osx_lol.txt
│   │   ├── osx_mami.txt
│   │   ├── osx_mokes.txt
│   │   ├── osx_mughthesec.txt
│   │   ├── osx_proton.txt
│   │   ├── osx_salgorea.txt
│   │   ├── osx_shlayer.txt
│   │   ├── osx_wirelurker.txt
│   │   ├── padcrypt.txt
│   │   ├── palevo.txt
│   │   ├── pandabanker.txt
│   │   ├── parasitehttprat.txt
│   │   ├── paycrypt.txt
│   │   ├── pdfjsc.txt
│   │   ├── pepperat.txt
│   │   ├── pghost.txt
│   │   ├── phorpiex.txt
│   │   ├── photominer.txt
│   │   ├── phytob.txt
│   │   ├── picgoo.txt
│   │   ├── pift.txt
│   │   ├── piratematryoshka.txt
│   │   ├── piritebot.txt
│   │   ├── plasmarat.txt
│   │   ├── plugx.txt
│   │   ├── ponmocup.txt
│   │   ├── ponystealer.txt
│   │   ├── poshcoder.txt
│   │   ├── pots.txt
│   │   ├── powelike.txt
│   │   ├── powerpool.txt
│   │   ├── powershell_injector.txt
│   │   ├── predatory.txt
│   │   ├── proslikefan.txt
│   │   ├── proxyback.txt
│   │   ├── psixbot.txt
│   │   ├── pterodo.txt
│   │   ├── pushdo.txt
│   │   ├── pykspa.txt
│   │   ├── pylocky.txt
│   │   ├── python_xwo.txt
│   │   ├── qakbot.txt
│   │   ├── qbot.txt
│   │   ├── qeallerrat.txt
│   │   ├── qrat.txt
│   │   ├── quadagent.txt
│   │   ├── quantloader.txt
│   │   ├── quasarrat.txt
│   │   ├── quasarstealer.txt
│   │   ├── qulabstealer.txt
│   │   ├── raccoon.txt
│   │   ├── rajump.txt
│   │   ├── rakhni.txt
│   │   ├── ramnit.txt
│   │   ├── ransirac.txt
│   │   ├── razy.txt
│   │   ├── reactorbot.txt
│   │   ├── redaman.txt
│   │   ├── rediswannamine.txt
│   │   ├── redsip.txt
│   │   ├── remcos.txt
│   │   ├── renocide.txt
│   │   ├── revcoderat.txt
│   │   ├── revengerat.txt
│   │   ├── reveton.txt
│   │   ├── revetrat.txt
│   │   ├── rincux.txt
│   │   ├── rombertik.txt
│   │   ├── rovnix.txt
│   │   ├── ruftar.txt
│   │   ├── runforestrun.txt
│   │   ├── rustock.txt
│   │   ├── sage.txt
│   │   ├── sakurel.txt
│   │   ├── sality.txt
│   │   ├── samsam.txt
│   │   ├── sanny.txt
│   │   ├── satana.txt
│   │   ├── sathurbot.txt
│   │   ├── satori.txt
│   │   ├── scarcruft.txt
│   │   ├── scranos.txt
│   │   ├── sdbot.txt
│   │   ├── seaduke.txt
│   │   ├── sefnit.txt
│   │   ├── selfdel.txt
│   │   ├── shadownet.txt
│   │   ├── shadowtechrat.txt
│   │   ├── shifu.txt
│   │   ├── shimrat.txt
│   │   ├── shiotob.txt
│   │   ├── shurl0ckr.txt
│   │   ├── shylock.txt
│   │   ├── siesta.txt
│   │   ├── silentbrute.txt
│   │   ├── silly.txt
│   │   ├── simda.txt
│   │   ├── sinkhole_360netlab.txt
│   │   ├── sinkhole_abuse.txt
│   │   ├── sinkhole_anubis.txt
│   │   ├── sinkhole_arbor.txt
│   │   ├── sinkhole_bitdefender.txt
│   │   ├── sinkhole_blacklab.txt
│   │   ├── sinkhole_bomccss.txt
│   │   ├── sinkhole_botnethunter.txt
│   │   ├── sinkhole_certgovau.txt
│   │   ├── sinkhole_certpl.txt
│   │   ├── sinkhole_changeip.txt
│   │   ├── sinkhole_checkpoint.txt
│   │   ├── sinkhole_cirtdk.txt
│   │   ├── sinkhole_collector.txt
│   │   ├── sinkhole_conficker.txt
│   │   ├── sinkhole_cryptolocker.txt
│   │   ├── sinkhole_dnssinkhole.txt
│   │   ├── sinkhole_doombringer.txt
│   │   ├── sinkhole_drweb.txt
│   │   ├── sinkhole_dynadot.txt
│   │   ├── sinkhole_dyre.txt
│   │   ├── sinkhole_farsight.txt
│   │   ├── sinkhole_fbizeus.txt
│   │   ├── sinkhole_fitsec.txt
│   │   ├── sinkhole_fnord.txt
│   │   ├── sinkhole_fraunhofer.txt
│   │   ├── sinkhole_gameoverzeus.txt
│   │   ├── sinkhole_georgiatech.txt
│   │   ├── sinkhole_gladtech.txt
│   │   ├── sinkhole_honeybot.txt
│   │   ├── sinkhole_hyas.txt
│   │   ├── sinkhole_kaspersky.txt
│   │   ├── sinkhole_kryptoslogic.txt
│   │   ├── sinkhole_microsoft.txt
│   │   ├── sinkhole_noip.txt
│   │   ├── sinkhole_oceanlotus.txt
│   │   ├── sinkhole_rsa.txt
│   │   ├── sinkhole_secureworks.txt
│   │   ├── sinkhole_shadowserver.txt
│   │   ├── sinkhole_sidnlabs.txt
│   │   ├── sinkhole_sinkdns.txt
│   │   ├── sinkhole_sobaken.txt
│   │   ├── sinkhole_sofacy.txt
│   │   ├── sinkhole_spamandabuse.txt
│   │   ├── sinkhole_sugarbucket.txt
│   │   ├── sinkhole_supportintel.txt
│   │   ├── sinkhole_switch.txt
│   │   ├── sinkhole_tech.txt
│   │   ├── sinkhole_tsway.txt
│   │   ├── sinkhole_turla.txt
│   │   ├── sinkhole_unknown.txt
│   │   ├── sinkhole_vicheck.txt
│   │   ├── sinkhole_virustracker.txt
│   │   ├── sinkhole_vittalia.txt
│   │   ├── sinkhole_wapacklabs.txt
│   │   ├── sinkhole_xaayda.txt
│   │   ├── sinkhole_yourtrap.txt
│   │   ├── sinkhole_zinkhole.txt
│   │   ├── skeeyah.txt
│   │   ├── skynet.txt
│   │   ├── skyper.txt
│   │   ├── sload.txt
│   │   ├── slserver.txt
│   │   ├── smokeloader.txt
│   │   ├── smsfakesky.txt
│   │   ├── snifula.txt
│   │   ├── snort.org.txt
│   │   ├── sockrat.txt
│   │   ├── sohanad.txt
│   │   ├── sonoko.txt
│   │   ├── spybotpos.txt
│   │   ├── spyeye.txt
│   │   ├── spygaterat.txt
│   │   ├── stabuniq.txt
│   │   ├── stealer.txt
│   │   ├── strongpity.txt
│   │   ├── supremebot.txt
│   │   ├── surtr.txt
│   │   ├── swamprat.txt
│   │   ├── symmi.txt
│   │   ├── synolocker.txt
│   │   ├── sysworm.txt
│   │   ├── ta505.txt
│   │   ├── tdss.txt
│   │   ├── teambot.txt
│   │   ├── teamspy.txt
│   │   ├── teerac.txt
│   │   ├── telebots.txt
│   │   ├── telegrab.txt
│   │   ├── terracotta.txt
│   │   ├── teslacrypt.txt
│   │   ├── tinba.txt
│   │   ├── tinynuke.txt
│   │   ├── tofsee.txt
│   │   ├── torpig.txt
│   │   ├── torrentlocker.txt
│   │   ├── tovkater.txt
│   │   ├── treasurehunter.txt
│   │   ├── trickbot.txt
│   │   ├── troldesh.txt
│   │   ├── tscookie.txt
│   │   ├── tupym.txt
│   │   ├── tvspy.txt
│   │   ├── unruy.txt
│   │   ├── up007.txt
│   │   ├── upatre.txt
│   │   ├── urlzone.txt
│   │   ├── ursnif.txt
│   │   ├── vaimalandra.txt
│   │   ├── vawtrak.txt
│   │   ├── vbcheman.txt
│   │   ├── vidar.txt
│   │   ├── vinderuf.txt
│   │   ├── virobot.txt
│   │   ├── virtum.txt
│   │   ├── virusrat.txt
│   │   ├── virut.txt
│   │   ├── vittalia.txt
│   │   ├── vjw0rm.txt
│   │   ├── vobfus.txt
│   │   ├── vssdestroy.txt
│   │   ├── vundo.txt
│   │   ├── waledac.txt
│   │   ├── wannacry.txt
│   │   ├── wannamine.txt
│   │   ├── waprox.txt
│   │   ├── wecorl.txt
│   │   ├── wecoym.txt
│   │   ├── weecnaw.txt
│   │   ├── winnti.txt
│   │   ├── wndred.txt
│   │   ├── wofeksad.txt
│   │   ├── wolfresearch.txt
│   │   ├── xadupi.txt
│   │   ├── xpay.txt
│   │   ├── xtrat.txt
│   │   ├── yenibot.txt
│   │   ├── yimfoca.txt
│   │   ├── zaletelly.txt
│   │   ├── zcrypt.txt
│   │   ├── zemot.txt
│   │   ├── zeroaccess.txt
│   │   ├── zeus.txt
│   │   ├── zherotee.txt
│   │   ├── zlader.txt
│   │   ├── zlob.txt
│   │   ├── zombieboy.txt
│   │   ├── zombrari.txt
│   │   ├── zonidel.txt
│   │   ├── zusy.txt
│   │   ├── zxshell.txt
│   │   └── zyklon.txt
│   └── plugins
│       ├── Backdoor_Analysis.py
│       ├── Backdoor_Analysis.pyc
│       ├── Config_Analysis.py
│       ├── Config_Analysis.pyc
│       ├── File_Analysis.py
│       ├── File_Analysis.pyc
│       ├── File_Check.py
│       ├── File_Check.pyc
│       ├── History_Analysis.py
│       ├── History_Analysis.pyc
│       ├── Host_Info.py
│       ├── Host_Info.pyc
│       ├── Log_Analysis.py
│       ├── Log_Analysis.pyc
│       ├── Network_Analysis.py
│       ├── Network_Analysis.pyc
│       ├── Proc_Analysis.py
│       ├── Proc_Analysis.pyc
│       ├── Rootkit_Analysis.py
│       ├── Rootkit_Analysis.pyc
│       ├── SSHAnalysis.py
│       ├── SSHAnalysis.pyc
│       ├── Search_File.py
│       ├── Search_File.pyc
│       ├── Sys_Init.py
│       ├── Sys_Init.pyc
│       ├── User_Analysis.py
│       ├── User_Analysis.pyc
│       ├── Webserver.py
│       ├── Webserver.pyc
│       ├── Webshell_Analysis.py
│       ├── Webshell_Analysis.pyc
│       ├── __init__.py
│       ├── __init__.pyc
│       └── webshell_rule
│           ├── WShell_APT_Laudanum.yar
│           ├── WShell_ASPXSpy.yar
│           ├── WShell_PHP_Anuna.yar
│           ├── WShell_PHP_in_images.yar
│           ├── WShell_THOR_Webshells.yar
│           ├── Wshell_ChineseSpam.yar
│           └── Wshell_fire2013.yar
├── sr
│   ├── result.md
│   └── sr.md
└── srp
    └── UbSec.md

20 directories, 909 files
```
